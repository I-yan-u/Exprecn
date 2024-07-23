"""
User History.
"""
from typing import Any, Union
from models.base import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.types import JSON
import json

class UserHistory(BaseModel, Base):
    __tablename__ = 'history'
    action = Column("Action", String(128))
    query = Column("Query", Text)
    user_id = Column("user_id", String(128), ForeignKey('user.id'))
    _result = Column("Result", JSON)
    _options = Column("Options", JSON)

    @hybrid_property
    def result(self):
        return self._result
    
    @hybrid_property
    def options(self):
        return self._options
    
    @result.setter
    def result(self, value: Union[str, list, tuple]):
        if isinstance(value, str):
            self._result = value
        elif isinstance(value, (list, tuple)):
            try:
                self._result = value
            except TypeError:
                raise ValueError("Result must be serializable to JSON")
        
    @options.setter
    def options(self, value):
        if isinstance(value, dict):
            self._options = value
        else:
            raise ValueError("Options must be a dictionary")
    
    # Establish the relationship with User
    user = relationship("User", back_populates="histories")

    def __init__(self, **kwargs) -> Any:
        """ Initialize the History object"""
        super().__init__(**kwargs)
