![pic](https://github.com/salamer/jolla/blob/master/pic/JOLLA.png)

# Jolla
jolla is a pure API server framework,and it is based on the gevent.

When I wrote Jolla,what I want to do is a high performance API server for you to simply obey its short rule,and get your calculation result fast be sent to browser or mobile for your service.so I made Jolla as simple as possible.

Hope you guys like it.

## INSTALL

```
pip install jolla
```

## DOCUMENT
wanna know more,please click [read more](http://salamer.github.io/jolla)

the Tutorial and documentation is [中文版](http://jolla.readthedocs.io/zh/latest/) [English edition](http://jolla-english.readthedocs.io/en/latest/)

## QUICKSTART
create a `app.py`,and write dowm:

```
from jolla import server,render,render_json

def index(request):
    return render('index.html')

def data(request):
    data = {'data': request['id']}
    return render_json(data)

class app(server.WebApp):
    urls = [
        (r'/', index),
        (r'/data/<id>', data),
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
