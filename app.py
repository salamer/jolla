from jolla import server
from jolla import plugins
from jolla import session
from jolla import HTTP404Error
from jolla import SessionError

session = session()


def index(request):
    return plugins.render('index.html')


def data(request):
    data = {'data': request['data']['ww']}
    return plugins.render_json(data)


def add(request):
    session.add_value('qq', 'ww')
    return 'yes'


def get(request):
    try:
        data = session.get_value('qq')
    except SessionError:
        raise HTTP404Error
    return data


class app(server.WebApp):
    urls = [
        (r'/', index),
        (r'/data', data),
        (r'/add', add),
        (r'/get', get)
    ]

if __name__ == '__main__':
    server = server.jolla_server(app)
    server.run_server()
