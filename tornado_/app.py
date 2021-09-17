import tornado.ioloop
import tornado.web
import controllers as controllers

def make_app():
    return tornado.web.Application([
        (r"/", controllers.MainHandler),
        (r"/err", controllers.ErrHandler),
        (r"/async", controllers.GoAsync),
        (r"/async_err_in", controllers.GoAsync_err_in_async),
        (r"/Weakref_TPT", controllers.Weakref_TPT),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(7000)
    tornado.ioloop.IOLoop.current().start()