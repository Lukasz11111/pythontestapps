import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
class EERR(tornado.web.RequestHandler):
    def get(self):
        raise "a"
        self.write("Hello, world")
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/err", EERR),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(6000)
    tornado.ioloop.IOLoop.current().start()