
import sys
sys.path.append("/app")
import tornado.web
import logging
from tests import test_ as t
from tests.regr import test_weakref
from tests.web import custom_code as C
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
        r = requests.get(f'{self.get_argument("RHOST")}', auth=('user', 'pass'),verify=False, timeout=10)
        self.write("Hello, world")

# class BaseHandler(tornado.web.RequestHandler):

#     def get_login_url(self):
#         return u"/login"

#     def get_current_user(self):
#         user_json = self.get_secure_cookie("user")
#         if user_json:
#             return tornado.escape.json_decode(user_json)
#         else:
#             return None

# class LoginHandler(BaseHandler):

#     def get(self):
#         self.write("aaa" )

#     def post(self):
#         username = self.get_argument("username", "")
#         password = self.get_argument("password", "")
#         # The authenticate method should match a username and password
#         # to a username and password hash in the database users table.
#         # Implementation left as an exercise for the reader.
#         auth = self.db.authenticate(username, password)
#         if auth:
#             self.set_current_user(username)
#             self.redirect(self.get_argument("next", u"/"))
#         else:
#             error_msg = u"?error=" + tornado.escape.url_escape("Login incorrect.")
#             self.redirect(u"/login" + error_msg)

#     def set_current_user(self, user):
#         if user:
#             self.set_secure_cookie("user", tornado.escape.json_encode(user))
#         else:
#             self.clear_cookie("user")

# class LogoutHandler(BaseHandler):

#     def get(self):
#         self.clear_cookie("user")
#         self.redirect(u"/login")

# # class CustomCodeCreate(tornado.web.RequestHandler):
# #     async def get(self):
# #         custom = C.CustomCode()

# #         err=f'''
# # raise 'You shall not pass!'
# #         '''
# #         custom.createNewPyFile("tmp", custom.codeGenDef(100, "a=2"), 1, err, "")

# #         self.write("Hello, world")

# # class CustomCodeCreateARGS(tornado.web.RequestHandler):
# #     async def get(self):
# #         custom = C.CustomCode()
# #         custom.createNewPyFile("tmp", f'{self.get_argument("CODE")}', f'{self.get_argument("REPLY")}', f'{self.get_argument("ENDCODE")}', f'{self.get_argument("STARTCODE")}')

# #         self.write("Hello, world")

# # class CustomCodeUse(tornado.web.RequestHandler):
# #     async def get(self):
# #         custom = C.CustomCode()
# #         custom.start("tmp",'0')
# #         # CustomCodeCreateArgs?CODE=print(%27a%27)&REPLY=100&ENDCODE=raise%20%27err%27&STARTCODE=
# #         self.write("Hello, world")
