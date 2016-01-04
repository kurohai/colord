import os
import cherrypy
from cherrypy import wsgiserver
from cherrypy.process.plugins import Daemonizer,PIDFile
from flask.ext.script import Manager
from flaskapp import flasktemplate, Base, engine


manager = Manager(flasktemplate)


@manager.command
def db():
    Base.metadata.create_all(bind=engine)


@manager.command
def quick():
    d = wsgiserver.WSGIPathInfoDispatcher({'/': flasktemplate})
    server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 80), d, server_name=flasktemplate.appname, )
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()


@manager.command
def go():
    flasktemplate.run(debug=True, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    manager.run()
