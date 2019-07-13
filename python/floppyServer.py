#!/usr/bin/env python
import cherrypy
import floppy

class FloppyServer(object):
    def form(self, message = "", notes="c/4 d/4 e/4"):
        return """<html>
          <head><title>Floppy!!!</title></head>
          <body>
            <p>%s<p>
            <form method="get" action="play">
              <div><textarea name="notes" rows="10">%s</textarea></div>
              <div><button type="submit">Play!</button></div>
            </form>
          </body>
        </html>""" % (message, notes)

    @cherrypy.expose
    def index(self):
        return self.form()

    @cherrypy.expose
    def play(self, notes):
        try:
            floppy.playNotes(notes)
            return self.form('Zahral som: %s' % notes, notes)
        except:
            return self.form('Aj by som zahral, ale toto nie su spravne noty: %s' % notes, notes)

cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.config.update({'server.socket_port': 80})
try:
    cherrypy.quickstart(FloppyServer())
finally:
    floppy.cleanup()
