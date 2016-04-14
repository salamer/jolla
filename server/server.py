
from gevent.pywsgi import WSGIServer
import re


def render(filename):
    with open(filename,"r") as f:
        res=f.read()

    return res

def index():
    return render("../templates/index.html")

def name():
    return render("../templates/name.html")


urls=[
    (r'/',index),
    (r'/name',name)
]



def application(environ,start_response):
    status='200 OK'

    header=[
        ('Content-Type','text/html')
    ]

    start_response(status,header)

    the_app=app(environ)

    html_code=the_app.parse()

    return html_code


class app():

    def __init__(self,environ):

        self._environ=environ

        self._path=self._environ['PATH_INFO']

        self.request={}

        self.request['method']=self._environ['REQUEST_METHOD']
        self.request['data']={}
        line=self._environ['QUERY_STRING']
        '''
        for i in line.spilt("&"):
            key,value=line.split("=")[0],line.split("=")[1]
            self.request['data'][key]=value
        '''

    def parse(self):
        for url_handler in urls:
            if url_handler[0]==self._path:
                html_code=url_handler[1]()
                return html_code
            else:
                return "404 NOT FOUND"


class jolla_server(WSGIServer):
    def __init__(self,app,port=8000,host="127.0.0.1"):
        self.port=port
        self.host=host
        self._app=app
        WSGIServer.__init__(self,listener=(self.host,self.port),application=self._app)

    def run_server(self):
        print "the server is running on the {} in the port {}".format(self.host,self.port)

        self.serve_forever()

if __name__=="__main__":
    server=jolla_server(application)
    server.run_server()
