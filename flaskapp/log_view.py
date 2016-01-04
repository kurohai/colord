
import os
import time
import codecs
import hashlib
from pprint import pprint
from flask import g, Blueprint, url_for
from flask import render_template, request
from flask.ext.login import LoginManager, current_user
from flask.ext.login import login_user, login_required, logout_user
from flask import Flask, render_template, request, url_for
from flask import abort, jsonify, redirect
from threading import Thread
from flask.ext.socketio import SocketIO, emit

from flaskapp import *

log_blueprint = Blueprint(
    'log_view',
    __name__,
    static_folder=None,
    static_url_path=None,
    template_folder=None,
    url_prefix=None,
    subdomain=None,
    url_defaults=None
)


@log_blueprint.route('/log/')
def get_log():
    """review app logs"""

    results = session.query(Log).all()
    logs = [repr(l) for l in results]
    data = '<br>\n'.join(logs)

    print(data)
    return render_template('public/index.html', data=data)


@log_blueprint.route('/log/delete/all/')
def delete_all_logs():
    """delete all logs"""
    print 'deleting all logs'

    count = 0
    for r in session.query(Log).all():
        count += 1
        session.delete(r)
        session.commit()

    data = 'Log deleted: {0}'.format(count)
    return render_template('public/index.html', data=data)
