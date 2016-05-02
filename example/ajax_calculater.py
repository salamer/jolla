from jolla import WebApp,jolla_server,render_json,render

def index(request):
    return render('index.html')

def add(request):
    return render_json({'answer':int(request['data']['a'])+int(request['data']['b'])})

class app(WebApp):
    urls = [
        (r'/', index),
        (r'/add', add)
    ]

if __name__ == '__main__':
    server = jolla_server(app)
    server.run_server()
