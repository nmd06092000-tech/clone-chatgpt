import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from database import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(
        UUID(as_uuid=True),
        primary_key= True,
        default = uuid.uuid4,
    )

    user_id = Column(
        UUID(as_uuid = True),
        ForeignKey("user.id"),
        nullable = False,
    )

    ai_modern_id = Column(
        UUID(as_uuid = True),
        ForeignKey("ai_modern.id"),
        nullable = False,
    )

    title = Column(String)

    last_message_at = Column(
        DateTime(timezone = True),
        server_default = func.now(),
    )

    created_at = Column(
        DateTime(timezone = True),
        server_default = func.now(),
    )

    update_at = Column(
        DateTime(timezone = True),
        server_default = func.now(),
        onupdate = func.now(),
    )

    user = relationship(
        "User",
        back_populates="conversations",
    )

    ai_modern = relationship(
        "AiModern",
        back_populates = "conversations",
    )

    message = relationship(
        "Message",
        back_populates = "conversation",
        cascade = "all,delete-orphan",
    )