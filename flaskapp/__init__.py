#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kurohai
# @Date:   2015-11-18 21:47:31
# @Last Modified by:   root
# @Last Modified time: 2016-01-04 07:22:04


from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy import create_engine, inspect
from sqlalchemy import MetaData, Table
from sqlalchemy.ext.declarative import *
from flask import Flask
import datetime
import os
from dicto import dicto
import flask.ext.restless
from flask.ext.socketio import SocketIO
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView

import settings

appname = settings.appname
appnamed = settings.appnamed
SECRET_KEY = settings.SECRET_KEY

pwd = os.path.abspath(os.curdir)

dbpath = '{dir}/{app}.db'.format(dir=pwd, app=appnamed)
dburi = 'sqlite:///{db}'.format(db=dbpath)


@as_declarative()
class BaseBase(dicto):

    def __hash__(self):
        return hash(self.id)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = BaseBase

engine = create_engine(dburi)
metadata = MetaData(bind=engine)
session = Session(engine)
db_session = scoped_session(
    sessionmaker(
        autocommit=True,
        autoflush=True,
        bind=engine
    )
)

Base.metadata = metadata
Base.query = db_session.query_property()


from models import *
from app import flasktemplate
from forms import *
from views import blueprint
from log_view import log_blueprint


flasktemplate.register_blueprint(blueprint)
flasktemplate.register_blueprint(log_blueprint)
