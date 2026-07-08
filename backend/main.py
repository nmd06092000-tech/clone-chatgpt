import uuid
from typing import List, Optional

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from database import Base, engine, get_db
from models.user import User
from models.ai_modern import AiMode
from models.conversation import Conversation
from models.message import Message

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


# ============
# Schemas
# ============

class HealthOut(BaseModel):
    status: str


class UserOut(BaseModel):
    id: uuid.UUID
    email: str
    display_name: str
    class Config:
        from_attributes = True


class AiModeOut(BaseModel):
    id: uuid.UUID
    key: str
    display_name: str
    class Config:
        from_attributes = True


class ConversationOut(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    ai_mode_id: uuid.UUID
    title: str
    last_message_at: Optional[str] = None
    class Config:
        from_attributes = True


class MessageOut(BaseModel):
    id: uuid.UUID
    conversation_id: uuid.UUID
    role: str
    content: str
    sequence_no: int
    class Config:
        from_attributes = True


class CreateUserIn(BaseModel):
    email: str
    password: str
    display_name: str = "User"


class CreateAiModeIn(BaseModel):
    key: str
    display_name: str


class CreateConversationIn(BaseModel):
    user_id: uuid.UUID
    ai_mode_id: uuid.UUID
    title: str = "New chat"


class CreateMessageIn(BaseModel):
    conversation_id: uuid.UUID
    role: str = Field(default="user")
    content: str


# ============
# Health
# ============

@app.get("/health", response_model=HealthOut)
def health():
    return {"status": "ok"}


# ============
# Seed / create basic
# ============

@app.post("/users", response_model=UserOut)
def create_user(payload: CreateUserIn, db: Session = Depends(get_db)):
    u = User(email=payload.email, password=payload.password, display_name=payload.display_name)
    db.add(u)
    db.commit()
    db.refresh(u)
    return u


@app.post("/ai-modes", response_model=AiModeOut)
def create_ai_mode(payload: CreateAiModeIn, db: Session = Depends(get_db)):
    m = AiMode(key=payload.key, display_name=payload.display_name)
    db.add(m)
    db.commit()
    db.refresh(m)
    return m


# ============
# Conversations
# ============

@app.get("/conversations", response_model=List[ConversationOut])
def list_conversations(
    user_id: Optional[uuid.UUID] = None,
    db: Session = Depends(get_db),
):
    q = db.query(Conversation)
    if user_id:
        q = q.filter(Conversation.user_id == user_id)

    # sort theo last_message_at desc, null xuống dưới
    q = q.order_by(Conversation.last_message_at.desc().nullslast(), Conversation.created_at.desc())
    return q.all()


@app.post("/conversations", response_model=ConversationOut)
def create_conversation(payload: CreateConversationIn, db: Session = Depends(get_db)):
    # validate FK tồn tại
    if not db.query(User).filter(User.id == payload.user_id).first():
        raise HTTPException(status_code=404, detail="User not found")
    if not db.query(AiMode).filter(AiMode.id == payload.ai_mode_id).first():
        raise HTTPException(status_code=404, detail="AI mode not found")

    c = Conversation(user_id=payload.user_id, ai_mode_id=payload.ai_mode_id, title=payload.title)
    db.add(c)
    db.commit()
    db.refresh(c)
    return c


# ============
# Messages
# ============

@app.get("/messages/{conversation_id}", response_model=List[MessageOut])
def list_messages(conversation_id: uuid.UUID, db: Session = Depends(get_db)):
    if not db.query(Conversation).filter(Conversation.id == conversation_id).first():
        raise HTTPException(status_code=404, detail="Conversation not found")

    return (
        db.query(Message)
        .filter(Message.conversation_id == conversation_id)
        .order_by(Message.sequence_no.asc())
        .all()
    )


@app.post("/messages", response_model=MessageOut)
def create_message(payload: CreateMessageIn, db: Session = Depends(get_db)):
    conv = db.query(Conversation).filter(Conversation.id == payload.conversation_id).first()
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found")

    last_seq = (
        db.query(Message.sequence_no)
        .filter(Message.conversation_id == payload.conversation_id)
        .order_by(Message.sequence_no.desc())
        .first()
    )
    next_seq = (last_seq[0] + 1) if last_seq else 1

    msg = Message(
        conversation_id=payload.conversation_id,
        role=payload.role,
        content=payload.content,
        sequence_no=next_seq,
    )
    db.add(msg)

    # cập nhật last_message_at để sort sidebar
    conv.last_message_at = func.now()

    db.commit()
    db.refresh(msg)
    return msg