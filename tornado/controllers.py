import tornado.web
#!/usr/bin/env python3

from tests import test_ as t
from tests.regr import test_weakref

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class ErrHandler(tornado.web.RequestHandler):
    def get(self):
        raise "You shall not pass"
        self.write("Hello, world")

class GoAsync(tornado.web.RequestHandler):
    def get(self):
        t.main()
        raise ""
        self.write("Hello, world")

class GoAsync_err_in_async(tornado.web.RequestHandler):
    async def get(self):
        await t.main_err()
        self.write("Hello, world")

class Weakref_TPT(tornado.web.RequestHandler):
    async def get(self):
        test_weakref.test_start()
        self.write("Hello, world")