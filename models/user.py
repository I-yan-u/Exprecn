"""
User Class
"""

from typing import Any
import uuid
from hashlib import md5
import sqlalchemy
from models.base import Base, BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    __tablename__ = 'user'
    email = Column("email", String(128), nullable=False)
    password = Column("password", String(128), nullable=False)
    first_name = Column("Firstname", String(128), nullable=True)
    last_name = Column("Lastname", String(128), nullable=True)

    # Establish the relationship with History
    histories = relationship("UserHistory", back_populates="user")

    def __init__(self, **kwargs):
        """Create the instance"""
        super().__init__(**kwargs)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "password":
            __value = md5(__value.encode()).hexdigest()
        super().__setattr__(__name, __value)