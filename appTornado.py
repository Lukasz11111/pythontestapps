import tornado.ioloop
import tornado.web
from tornadoApp import controllers as controllers
import git
import revdebug as rdb

def make_app():
    return tornado.web.Application([
        (r"/", controllers.MainHandler),
        (r"/err", controllers.ErrHandler),
        (r"/async", controllers.GoAsync),
        (r"/async_err_in", controllers.GoAsync_err_in_async),
        (r"/Weakref_TPT", controllers.Weakref_TPT),
        (r"/atexit", controllers.Atexit),
        
    ])


if __name__ == "__main__":
    
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    rdb.release=sha

    app = make_app()
    app.listen(7000)
    tornado.ioloop.IOLoop.current().start()
