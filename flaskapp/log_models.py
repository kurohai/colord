from sqlalchemy import Column
from sqlalchemy.types import DateTime, Integer, String
import datetime
from sqlalchemy import Column, ForeignKey, Float
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


getcontext().prec = 2
getcontext()

from flaskapp import Base


def start_last_tick():
    return time.mktime(datetime.datetime.now().timetuple())


class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)  # auto incrementing
    logger = Column(String)  # the name of the logger. (e.g. myapp.views)
    level = Column(String)  # info, debug, or error?
    trace = Column(String)  # the full traceback printout
    msg = Column(String)  # any custom log you may have included
    created_at = Column(DateTime, default=datetime.datetime.now)  # the current timestamp

    def __init__(self, logger=None, level=None, trace=None, msg=None):
        self.logger = logger
        self.level = level
        self.trace = trace
        self.msg = msg

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        return "{log}\t{t}: {0} - {1}".format(self.created_at.strftime('%Y-%m-%d %H:%M:%S'), self.msg, t=self.level, log=self.logger)
