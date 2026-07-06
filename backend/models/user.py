import uuid

from sqlanchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column