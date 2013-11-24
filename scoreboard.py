import os.path
import cherrypy
from cherrypy.lib.static import serve_file

class Root(object):
    @cherrypy.expose
    def default(self, *args, **kwargs):
        if len(args) == 0:
            return serve_file(os.path.join(current_dir, 'app', 'index.html'))
        else:
            return serve_file(os.path.join(current_dir, 'app', *args))

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    cherrypy.quickstart(Root(), '/')