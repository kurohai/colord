#!/bin/env python

from flask import Flask
from flask.ext.pagedown import PageDown
from flaskext.markdown import Markdown
import settings

flasktemplate = Flask(__name__)
flasktemplate.appname = settings.appname
flasktemplate.appnamed = settings.appnamed
flasktemplate.config.SECRET_KEY = settings.SECRET_KEY
flasktemplate.config.SESSION_PROTECTION = settings.SESSION_PROTECTION

pagedown = PageDown(flasktemplate)
Markdown(flasktemplate)


@flasktemplate.template_global()
def appname():
    return flasktemplate.appname


@flasktemplate.template_global()
def appnamed():
    return flasktemplate.appnamed


@flasktemplate.errorhandler(404)
def error_not_found(error):
    """Render a custom template when responding with 404 Not Found."""
    return 'No page here, dood. 404!', 404
