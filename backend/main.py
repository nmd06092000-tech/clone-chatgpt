from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base
from database import engine
from database import SessionLocal

from models.user import User
from models.ai_modern import AiModern
from models.conversation import Conversation
from models.message import Message

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)


# =========================
# Health Check
# =========================

@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# =========================
# Test APIs
# =========================

@app.get("/create-user")
def create_user():

    db = SessionLocal()

    user = User(
        username="duc"
    )

    db.add(user)
    db.commit()

    db.close()

    return {
        "message": "created"
    }


@app.get("/create-conversation")
def create_conversation_test():

    db = SessionLocal()

    conversation = Conversation(
        title="Vue Learning"
    )

    db.add(conversation)
    db.commit()

    db.close()

    return {
        "message": "created"
    }


@app.get("/create-message")
def create_message_test():

    db = SessionLocal()

    message = Message(
        conversation_id=1,
        role="user",
        content="Vue là gì?"
    )

    db.add(message)
    db.commit()

    db.close()

    return {
        "message": "created"
    }


# =========================
# Conversations
# =========================

@app.get("/conversations")
def get_conversations():

    db = SessionLocal()

    conversations = (
        db.query(Conversation)
        .all()
    )

    db.close()

    return conversations


# =========================
# Messages
# =========================

@app.get("/messages/{conversation_id}")
def get_messages(
    conversation_id: int
):

    db = SessionLocal()

    messages = (
        db.query(Message)
        .filter(
            Message.conversation_id == conversation_id
        )
        .all()
    )

    db.close()

    return messages