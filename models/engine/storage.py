"""
Database storage engine
"""
import models
from models.base import Base, BaseModel
from models.user import User
from models.history import UserHistory
from os import getenv
from config import DB, ENV
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

classes = {'User': User, 'UserHistory': UserHistory}

user = getenv('DB_USER') or DB['user']
password = getenv('DB_PASS') or DB['password']
host = getenv('DB_HOST') or DB['host']
db = getenv('DB_NAME') or DB['database']

run_type = getenv('RUNSTAGE') or ENV['stage']


class DB:
    __session = None
    __engine = None

    def __init__(self):
        db_url = f'mysql+mysqldb://{user}:{password}@{host}/{db}'
        self.__engine = create_engine(db_url)
        Base.metadata.create_all(bind=self.__engine)
        
        if run_type == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id=None):
        """ call get() method on objects"""
        if cls not in classes.values():
            return None
        all_cls = models.store.all(cls).values()
        if id is None:
            return [value for value in all_cls]
        else:
            for value in all_cls:
                if value.id == id:
                    return value
        return None
    
    def get_user_email(self, email=None):
        """ call get() method on objects"""
        all_user = models.store.all(User).values()
        if email is None:
            return [value for value in all_user]
        else:
            for value in all_user:
                if value.email == email:
                    return value
        return None
    
    def get_hist_user(self, user_id, id=None):
        """ call get() method on objects"""
        all_hist = models.store.all(UserHistory).values()
        if id is None:
            return [value for value in all_hist if value.user_id == user_id]
        else:
            for value in all_hist:
                if value.user_id == user_id and value.id == id:
                    return value
        return None
    
    def count(self, cls=None):
        """counts individual class object"""
        all_cls = classes.values()

        if not cls:
            count = 0
            for value in all_cls:
                count += len(models.store.all(value).values())
        else:
            count = len(models.store.all(cls).values())
        return count
