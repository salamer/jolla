![pic](https://github.com/salamer/jolla/blob/master/pic/JOLLA.png)

# Jolla
jolla is a pure API server framework,and it is based on the gevent.

> still being constrating

version:1.1.0
- basic work have done,it's already a api server for api collect.
- delete the statics function,if you wanna css or js,use cdn or server like nginx and apache httpd;

## INSTALL

```
sudo pip install jolla

```

##DOCUMENTATION

wanna know more,please click [doc](http://salamer.github.io/jolla)

## QUICKSTART
create a `app.py`,and write dowm:

```
from jolla import server,SessionError,plugins,session,HTTP404Error

session = session()


def index(request):
    return plugins.render('index.html')

def chinese(request):
    try:
        if request['data']['ww']=='海贼王':
            return 'great anime'
    except:
        pass
    return 'yeah!chinese'


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
        (r'/chinese',chinese)
    ]

if __name__ == '__main__':
    server = server.jolla_server(app)
    server.run_server()
```

and then,run:

```
python app.py
```

and open the [http://127.0.0.1:8000](http://127.0.0.1:8000) on your browser

you will see the magic happen!

## LICENSE
Copyright © 2016 by Aljun

Under Apache license : [http://www.apache.org/licenses/](http://www.apache.org/licenses/)
