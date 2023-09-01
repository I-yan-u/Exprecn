"""
User History.
"""
from typing import Any
from models.base import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class UserHistory(BaseModel, Base):
    __tablename__ = 'history'
    action = Column("Action", String(128))
    query = Column("Query", String(128))
    user_id = Column("user_id", String(128), ForeignKey('user.id'))
    
    # Establish the relationship with User
    user = relationship("User", back_populates="histories")

    def __init__(self, **kwargs) -> Any:
        """ Initialize the History object"""
        super().__init__(**kwargs)