from sanic import Sanic
from sanic.response import json

app = Sanic("My Hello, world app")

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.route('/err')
async def test(request):
    raise "You shall not pass!"
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)