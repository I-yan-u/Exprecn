"""
User Class
"""

from datetime import datetime
from typing import Any
from hashlib import md5
from models.base import Base, BaseModel
from sqlalchemy import Column, String, Integer, LargeBinary
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    __tablename__ = 'user'
    email = Column("email", String(128), nullable=False)
    password = Column("password", String(128), nullable=False)
    first_name = Column("Firstname", String(128), nullable=False)
    last_name = Column("Lastname", String(128), nullable=False)
    Bio = Column("Bio", String(250), nullable=True)
    website = Column("Website", String(250), nullable=True)
    image = Column("Image", LargeBinary, nullable=True)
    admin = Column("Admin", Integer, default=0)
    reset_token = Column("ResetToken", String(128), nullable=True)
    otp = Column("OTP", Integer, nullable=True)
    
    # Establish the relationship with History
    histories = relationship("UserHistory", back_populates="user",
                              cascade="all, delete, delete-orphan") 

    def __init__(self, **kwargs):
        """Create the instance"""
        super().__init__(**kwargs)

    def update(self, **kwargs):
        """Update the instance"""
        time_now = datetime.utcnow()
        for k, v in kwargs.items():
            if k not in ['id', 'created_at', 'updated_at', 'password', 'image', 'admin', 'reset_token', 'otp']:
                setattr(self, k, v)
        setattr(self, 'updated_at', time_now)
        self.save()

    # def __setattr__(self, __name: str, __value: Any) -> None:
    #     if __name == "password":
    #         __value = md5(__value.encode()).hexdigest()
    #     super().__setattr__(__name, __value)