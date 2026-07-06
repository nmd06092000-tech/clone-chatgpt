import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    email = Column(
        String,
        unique = True,
        nullable = False,
    )

    display_name = Column(
        String,
        nullable = False,
    )

    created_at = Column(
        DateTime(timezone = True),
        server_default = func.now(),
    )

    updated_at = Column(
        DateTime(timezone = True),
        server_default = func.now(),
        onupdate = func.now(),
    )

    conservations = relationship(
        "Conversation",
        back_populates = "user",
    )