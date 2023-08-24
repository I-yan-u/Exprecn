"""
User History.
"""

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserHistory(Base):
    __tablename__ = 'history'