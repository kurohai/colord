import os
import cherrypy
from cherrypy import wsgiserver
from cherrypy.process.plugins import Daemonizer,PIDFile
from flask.ext.script import Manager
from flaskapp import flasktemplate, Base, engine, Color, ColorSet, session
from pprint import pprint

manager = Manager(flasktemplate)


@manager.command
def db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    data()


@manager.command
def data():
    day = ColorSet()

    yellow = Color()
    yellow.name = 'yellow'
    yellow.colorset = day

    white = Color()
    white.name = 'white'
    white.colorset = day

    pink = Color()
    pink.name = 'pink'
    pink.colorset = day

    purple = Color()
    purple.name = 'purple'
    purple.colorset = day

    olive = Color()
    olive.name = 'olive'
    olive.colorset = day

    azure = Color()
    azure.name = 'azure'
    azure.colorset = day

    camo = Color()
    camo.name = 'camo'
    camo.colorset = day

    session.add(day)
    session.add(yellow)
    session.add(white)
    session.add(pink)
    session.add(purple)
    session.add(olive)
    session.add(azure)
    session.add(camo)
    session.commit()

    d = session.query(ColorSet).all()
    for i in d:
        print i.date
        print i.id
        for c in i.color:
            print c.name


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
