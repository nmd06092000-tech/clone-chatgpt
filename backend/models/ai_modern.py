import uuid

from sqlalchemy import Column
from sqlalchemy import String

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship

from database import Base

class AiModern(Base):
    __tablename__ = "ai_modern"

    id = Column(
        UUID(as_uuid=True),
        primary_key = True,
        default = uuid.uuid4,
    )

    display_name = Column(
        String,
        nullable = False,
    )

    conversations = relationship(
        "Conversation",
        back_populates = "ai_mode",
    )