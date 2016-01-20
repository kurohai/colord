from sqlalchemy import Column, Table
from sqlalchemy.types import DateTime, Integer, String
import datetime
from sqlalchemy import Column, ForeignKey, Float, Date
from sqlalchemy import Boolean, DateTime, Integer
from sqlalchemy import String, Text, BigInteger
from sqlalchemy.orm import relationship, synonym
from sqlalchemy.ext.declarative import declarative_base
from werkzeug import check_password_hash, generate_password_hash
from flask.ext.login import AnonymousUserMixin
from sqlalchemy.ext.declarative import *
from dicto import dicto
import time
from decimal import *
from flaskapp import Base
from log_models import *



class BaseMixin(dicto):
    """docstring for BaseMixin"""
    def __init__(self):
        super(BaseMixin, self).__init__()
        
class User(Base):

    """A user login, with credentials and authentication."""
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.datetime.now)
    modified = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    admin = Column(Boolean, default=False)
    name = Column('name', String(200))
    username = Column(String(100), unique=True, nullable=False)
    active = Column(Boolean, default=True)
    email = Column(String(100), unique=True, nullable=False)
    _password = Column('password', String(100))

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        if password:
            password = password.strip()
        self._password = generate_password_hash(password)

    password_descriptor = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password_descriptor)

    def check_password(self, password):
        if self.password is None:
            return False
        password = password.strip()
        if not password:
            return False
        return check_password_hash(self.password, password)

    @classmethod
    def authenticate(cls, query, username, password):
        username = username.strip().lower()
        user = query(cls).filter(cls.username == username).first()
        if user is None:
            return None, False
        if not user.active:
            return user, False
        return user, user.check_password(password)

    # Hooks for Flask-Login.
    #
    # As methods, these are only valid for User instances, so the
    # authentication will have already happened in the view functions.
    #
    # If you prefer, you can use Flask-Login's UserMixin to get these methods.

    def get_id(self):
        return str(self.id)

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_admin(self):
        return self.admin

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id} Username: {self.username}>'.format(self=self)


class ColorSet(Base):
    """docstring for ColorSet"""
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, default=datetime.datetime.today, unique=True)

    colors = relationship(
        'Color',
        backref='colorset',
        primaryjoin="ColorSet.id==Color.colorset_id",
    )


class Color(Base):
    """docstring for Color"""
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    colorset_id = Column(Integer, ForeignKey('colorset.id'))
