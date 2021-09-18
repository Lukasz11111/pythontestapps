import tornado.ioloop
import tornado.web
from tornadoApp import controllers as controllers
import git
import revdebug as rdb

import logging
global routs

def make_app():
    global routs
    routs=[
        (r"/", MainHandler),
        (r"/err", controllers.ErrHandler),
        (r"/async", controllers.GoAsync),
        (r"/async_err_in", controllers.GoAsync_err_in_async),
        (r"/Weakref_TPT", controllers.Weakref_TPT),
        (r"/atexit", controllers.Atexit),  
    ]
    return tornado.web.Application(routs)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        result=''
        for x,v in routs:
            result=result+f'<br/><a href={x}>{x}<a>'
        self.write(str(result))

class GetHandler(tornado.web.RequestHandler):
    def get(self):
        key = self.get_argument('key', None)
        response = {'key': key}
        self.write(response)

if __name__ == "__main__":
    
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    rdb.release=sha
    
    app = make_app()

    app.listen(7000)
    tornado.ioloop.IOLoop.current().start()
