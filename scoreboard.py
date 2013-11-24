import os.path
import cherrypy
import json
from cherrypy.lib.static import serve_file

class Teams:
    exposed = True
    
    def __init__(self):
        self.teams = { '1': 'Team 1', '2': 'Team 2' }
    
    def GET(self, id=None):
        if id == None:
            return json.dumps(self.teams)
        elif id in teams:
            return json.dumps(self.teams[id])
        else:
            return "ERROR"
            
    def PUT(self, id, name=None):
        print(name)
        if id in self.teams and name != None:
            self.teams[id] = name

class Root(object):
    @cherrypy.expose
    def default(self, *args, **kwargs):
        if len(args) == 0:
            return serve_file(os.path.join(current_dir, 'app', 'index.html'))
        else:
            return serve_file(os.path.join(current_dir, 'app', *args))

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    cherrypy.tree.mount(
        Root(), '/',
        {'/':
            {'request.dispatch': cherrypy.dispatch.Dispatcher()}
        }
    )
    
    cherrypy.tree.mount(
        Teams(), '/api/teams',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    
    cherrypy.engine.start()
    cherrypy.engine.block()