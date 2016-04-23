import gevent.monkey
gevent.monkey.patch_all()

from gevent.pywsgi import WSGIServer
import re

from HTTPerror import HTTP404Error


def render(filename):
    with open(filename, "r") as f:
        res = f.read()

    return res


def index():
    return render("../templates/index.html")


def name():
    return render("../templates/name.html")


urls = [
    (r'/', index),
    (r'/name', name)
]


def application(environ, start_response):

    the_app = app(environ)

    try:
        html_code = the_app.parse()
        status = '200 OK'
    except HTTP404Error:
        status = '404 NOT FOUND'
        html_code = render("../templates/404.html")

    header = [
        ('Content-Type', 'text/html')
    ]

    start_response(status, header)

    return html_code


class app():

    def __init__(self, environ):

        self._environ = environ

        self._path = self._environ['PATH_INFO']

        self.request = {}

        self.request['method'] = self._environ['REQUEST_METHOD']
        self.request['data'] = {}
        line = self._environ['QUERY_STRING']

    def parse(self):
        for url_handler in urls:
            if url_handler[0] == r'/':
                if self._environ['PATH_INFO'] != '/':
                    continue
                else:
                    html_code = url_handler[1]()

            if re.match(self._environ['PATH_INFO'], url_handler[0]):
                html_code = url_handler[1]()
                return html_code
            else:
                raise HTTP404Error('REQUEST NOT FOUND IN ROUTE CONFIGURATION')


class jolla_server(WSGIServer):

    def __init__(self, app, port=8000, host="127.0.0.1"):
        self.port = port
        self.host = host
        self._app = app
        WSGIServer.__init__(self, listener=(
            self.host, self.port), application=self._app)

    def run_server(self):
        print "the server is running on the {} in the port {}".format(self.host, self.port)

        self.serve_forever()

if __name__ == "__main__":
    server = jolla_server(application)
    server.run_server()
