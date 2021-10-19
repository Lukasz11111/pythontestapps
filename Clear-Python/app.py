import tornado.ioloop
import tornado.web
import requests

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class Req(tornado.web.RequestHandler):
    def get(self):
        r = requests.get(f'{self.get_argument("RHOST")}', auth=('user', 'pass'))
        self.write("Hello, world")

      

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/req", Req),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(6999)
    tornado.ioloop.IOLoop.current().start()