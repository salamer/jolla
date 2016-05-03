#!/usr/bin/env python
# -*- coding: utf-8 -*-


from jolla import server
from jolla import plugins
from jolla import session
from jolla import HTTP404Error
from jolla import SessionError

session = session()


def index(request):
    return plugins.render('index.html')


def chinese(request):
    try:
        if request['data']['ww'] == '海贼王':
            return 'great anime'
    except:
        pass
    return 'yeah!'


def data(request):
    data = {'data': request['id']}
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


def blog(request):
    if request['method'] == 'GET':
        return plugins.render_json({'name': session.get_value('name')})
    else:
        if request['method'] == 'POST':
            session.add_value('name', request['data']['name'])
            return 'ok'


class app(server.WebApp):
    urls = [
        (r'/', index),
        (r'/data/<id>', data),
        (r'/data', data),
        (r'/add', add),
        (r'/get', get),
        (r'/blog', blog),
        (r'/chinese', chinese)
    ]

if __name__ == '__main__':
    server = server.jolla_server(app)
    server.run_server()
