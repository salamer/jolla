![pic](https://github.com/salamer/jolla/blob/master/pic/JOLLA.png)

#Jolla

jolla is a pure API server framework,and it based on the gevent.

> still being constrating

##QUICKSTART

add a `app.py`,and write dowm:

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

and then,run:

    python app.py

and open the http://127.0.0.1:8000 on your browser

you will see the magic happen!

##LICENSE


Copyright © 2016 by Aljun

Under Apache license : [http://www.apache.org/licenses/](http://www.apache.org/licenses/)
