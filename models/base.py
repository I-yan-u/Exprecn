"""
Base clase for database objects
"""

from typing import Any
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()

class BaseModel:
    """ Base class for database models"""
    id = Column("id", String(128), primary_key=True)

    def __init__(self, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())

    def __str__(self):
        """ returns a string representation of the object"""
        return "({}) - [{}]".format(self.__class__.__name__, self.__dict__)
    
    def save(self):
        """ saves the object"""
        models.store.new(self)
        models.store.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if "password" in new_dict:
            del new_dict["password"]
        return new_dict
    
    def delete(self):
        """delete the current instance from the storage"""
        models.store.delete(self)