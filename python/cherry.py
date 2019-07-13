#!/usr/bin/env python
import cherrypy

class FloppyServer(object):
    @cherrypy.expose
    def index(self):
        return 'Ahoj!'
    @cherrypy.expose
    def play(self, notes):
        return 'Aj by som zahral noty: %s' % notes

cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.config.update({'server.socket_port': 80})
cherrypy.quickstart(FloppyServer())
