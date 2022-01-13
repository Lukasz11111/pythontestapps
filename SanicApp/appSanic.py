from sanic import Sanic
from sanic.response import json
from sanic.request import RequestParameters
import requests
import sys
sys.path.append("/app")
from tests.web import asyncio as asyncTest
app = Sanic("My Hello, world app")
from skywalking import agent, config

config.log_reporter_active=True

@app.route('/')
async def test(request):
    agent.logger.info("SW test log %s %s %s", 'arg0', 'arg1', 'arg2')
    return json({'hello': 'world'})

@app.route('/err')
async def err(request):
    raise "You shall not pass!"
    return json({'hello': 'world'})

@app.route('/req')
async def req(request):
    r = requests.get(f'{request.args["RHOST"][0]}', auth=('user', 'pass'),verify=False, timeout=10)
    return json({'hello': 'world'})


@app.route('/req-async')
async def reqAsync(request):
    await asyncTest.reqAsync(f'{request.args["RHOST"][0]}')
    return json({'hello': 'world'})

@app.route('/async')
async def reqAsync(request):
    await asyncTest.asyncSleepTest(1)
    return json({'hello': 'world'})

@app.route('/async-err')
async def reqAsync(request):
    await asyncTest.asyncSleepTestErr(1)
    return json({'hello': 'world'})

@app.route('/async-while')
async def reqAsync(request):
    await asyncTest.asyncWhile()
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)