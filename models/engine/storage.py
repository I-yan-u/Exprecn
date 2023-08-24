"""
Database storage engine
"""
from typing import Any
from models.user import User
from models.history import UserHistory
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {'User': User, 'UserHistory': UserHistory}

class DB:
    __session = None
    __engine = None

    def __init__(self) -> Any:
        db_url = 'mysql+mysqldb://root:iyanu@localhost/exprecn_db'
        self.__engine = create_engine(db_url)

