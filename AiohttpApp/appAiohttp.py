
import requests
import sys
sys.path.append("/app")
from tests.web import asyncio as asyncTest

#!/usr/bin/env python3
from aiohttp import web

import asyncio
import time
import logging
from skywalking import agent, config

config.log_reporter_active=True
logging.basicConfig(filename="file.log", level=logging.DEBUG)


async def err(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    raise "You shall not pass!"
    return web.Response(text=text)

async def req(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    r = requests.get(f'{request.args["RHOST"][0]}', auth=('user', 'pass'),verify=False, timeout=10)
    return web.Response(text=text)

async def reqAsync(request):
    import os

    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    # a=request.rel_url.query['RHOST']
    await asyncTest.reqAsync(f'{str((request.query["RHOST"]))}')

    text=f'''
------------------------------------------------------------------------------------------------------------------------
    {str((request.query['RHOST']))}
------------------------------------------------------------------------------------------------------------------------

    '''


    return web.Response(text=text)


async def asyncSleepTest(request):
    text="hello"
    await asyncio.sleep(1)
    async def a():
        await asyncio.sleep(1)
    await a()
    return web.Response(text=text)

async def asyncSleepTestErr(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    await asyncTest.asyncSleepTestErr(1)
    return web.Response(text=text)


async def asyncWhile(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    await asyncTest.asyncWhile()
    return web.Response(text=text)


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, "
    # logger = logging.getLogger('spam_application')
    # logger.setLevel(logging.INFO)
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')

    return web.Response(text=text)

import random
import string



async def asyncSleepTestErrZeroDivisionError(request):
    import os
    name =""
    text_=(''.join(random.choices(string.ascii_uppercase + string.digits, k=25)))
    revdebug.cfg.version=text_
    print(os.getenv('REVDEBUG_RELEASE'))
    os.environ["REVDEBUG_RELEASE"] = text_
    print(os.getenv('REVDEBUG_RELEASE'))
    return web.Response(text=name)


# async def asyncSleepTestErrZeroDivisionError(request):
#     name =""
#     text_=(''.join(random.choices(string.ascii_uppercase + string.digits, k=25)))
#     raise ZeroDivisionError(text_)
#     return web.Response(text=name)

async def asyncSleepTestErNameErrorr(request):
    name =""
    text_=(''.join(random.choices(string.ascii_uppercase + string.digits, k=25)))
    raise NameError(text_)
    return web.Response(text=name)
async def asyncSleepTestErrTypeError(request):
    name =""
    text_=(''.join(random.choices(string.ascii_uppercase + string.digits, k=25)))
    raise TypeError(text_)
    return web.Response(text=name)
async def asyncSleepTestErrOSError(request):
    name =""
    text_=(''.join(random.choices(string.ascii_uppercase + string.digits, k=25)))
    raise OSError(text_)
    return web.Response(text=name)
async def asyncSleepTestErrValueErrorValueError(request):
    name =""
    text_=(''.join(random.choices(string.ascii_uppercase + string.digits, k=25)))
    raise ValueError(text_)
    return web.Response(text=name)
async def asyncSleepTestErrBaseException(request):
    name =""
    text_=(''.join(random.choices(string.ascii_uppercase + string.digits, k=25)))
    raise BaseException(text_)
    return web.Response(text=name)
async def asyncSleepTestErrException(request):
    name =""
    text_=(''.join(random.choices(string.ascii_uppercase + string.digits, k=25)))
    raise Exception(text_)
    return web.Response(text=name)

async def asyncSleepTestErrConnectionError(request):
    name =""
    text_=(''.join(random.choices(string.ascii_uppercase + string.digits, k=25)))
    raise ConnectionError(text_)
    return web.Response(text=name)

app = web.Application()
app.add_routes([
    web.get('/', handle),
    web.get('/req', req),
    web.get('/req-async', reqAsync),
    web.get('/err', err),
    web.get('/asyncSleepTestErrConnectionError', asyncSleepTestErrConnectionError),
    web.get('/asyncSleepTestErrException', asyncSleepTestErrException),
    web.get('/asyncSleepTestErrBaseException', asyncSleepTestErrBaseException),
    web.get('/asyncSleepTestErrValueErrorValueError', asyncSleepTestErrValueErrorValueError),
    web.get('/asyncSleepTestErrOSError', asyncSleepTestErrOSError),
    web.get('/asyncSleepTestErrTypeError', asyncSleepTestErrTypeError),
    web.get('/asyncSleepTestErNameErrorr', asyncSleepTestErNameErrorr),
    web.get('/asyncSleepTestErrZeroDivisionError', asyncSleepTestErrZeroDivisionError),
    web.get('/asyncWhile', asyncWhile),
    ])

if __name__ == '__main__':
    web.run_app(app, port=7000)



