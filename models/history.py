"""
User History.
"""
from typing import Any
from models.base import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

class UserHistory(BaseModel, Base):
    __tablename__ = 'history'
    action = Column("Action", String(128))
    query = Column("Query", Text)
    user_id = Column("user_id", String(128), ForeignKey('user.id'))
    result = Column("Result", Text)
    
    # Establish the relationship with User
    user = relationship("User", back_populates="histories")

    def __init__(self, **kwargs) -> Any:
        """ Initialize the History object"""
        super().__init__(**kwargs)