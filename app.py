from jolla import server
from jolla import plugins

def index():
    return plugins.render('templates/index.html')

class app(server.WebApp):
    urls=[
        (r'/',index)
    ]

if __name__=='__main__':
    server=server.jolla_server(app)
    server.run_server()
