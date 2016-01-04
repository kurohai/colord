#!/bin/env python

from flask import Flask
from flask.ext.pagedown import PageDown
from flaskext.markdown import Markdown


flasktemplate = Flask(__name__)
flasktemplate.appname = 'Flask Template'
flasktemplate.appnamed = 'flasktemplate'
flasktemplate.config.SECRET_KEY = 'enydM2ANhdcoKwdVa0jWvEsbPFuQpMjf'
flasktemplate.config.SESSION_PROTECTION = 'strong'

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
