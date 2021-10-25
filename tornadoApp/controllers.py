import tornado.web
import logging
from tests import test_ as t
from tests.regr import test_weakref
from tests.web import custom_code
# from tests.db import test_pg_rdb

import requests

class ErrHandler(tornado.web.RequestHandler):
    def get(self):
        raise "You shall not pass!!"
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

class Test_user_serialization_inheritance(tornado.web.RequestHandler):
    async def get(self):
        from tests.regr import test_user_serialization_inheritance
        test_user_serialization_inheritance
        self.write("Hello, world")
        
class Atexit(tornado.web.RequestHandler):
    async def get(self):
        from tests.regr import test_atexit
        test_atexit
        self.write("Hello, world")
        
class Req(tornado.web.RequestHandler):
    async def get(self):
        r = requests.get(f'{self.get_argument("RHOST")}', auth=('user', 'pass'))
        self.write("Hello, world")

class CustomCodeCreate(tornado.web.RequestHandler):
    async def get(self):
        custom = customCode.CustomCode()

        err=f'''
        raise 'You shall not pass!'
        '''
        custom.createNewPyFile("tmp", custom.codeGenDef(100, "a=2"), 1, err, "")

        self.write("Hello, world")

class CustomCodeUse(tornado.web.RequestHandler):
    async def get(self):
        custom = customCode.CustomCode()
        custom.start("tmp",'0')
        
        self.write("Hello, world")
