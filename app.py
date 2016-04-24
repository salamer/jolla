from jolla import server
from jolla import plugins


def index(request):
    return plugins.render('index.html')


def data(request):
    data = {'data':request['data']['ww']}
    return plugins.render_json(data)


class app(server.WebApp):
    urls = [
        (r'/', index),
        (r'/data', data)

    ]

if __name__ == '__main__':
    server = server.jolla_server(app)
    server.run_server()
