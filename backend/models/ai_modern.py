import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database import Base


class AiMode(Base):
    __tablename__ = "ai_modes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    key = Column(String, unique=True, index=True, nullable=False)        # vd: "gpt-4o-mini"
    display_name = Column(String, nullable=False)                        # vd: "GPT-4o mini"

    conversations = relationship("Conversation", back_populates="ai_mode")