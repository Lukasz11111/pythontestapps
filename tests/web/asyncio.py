
import asyncio
import aiohttp


async def reqAsync(host):
    async with aiohttp.ClientSession() as session:
        async with session.get(host) as resp:
            print(resp.status)

async def asyncSleepTest(time):
    await asyncio.sleep(time)
    async def a():
        await asyncio.sleep(time)
    await a()
    print("a")
async def asyncSleepTestErr(time):
    await asyncio.sleep(time)
    async def a():
        await asyncio.sleep(time)
        raise "You shall not pass!"
    await a()

# #!/usr/bin/env python3
# from aiohttp import web
# # from skywalking import agent; agent.start()
# async def handle(request):
#     name = request.match_info.get('name', "Anonymous")
#     text = "Hello, " + name
#     1 / 0
#     return web.Response(text=text)
# app = web.Application()
# app.add_routes([web.get('/', handle),
# web.get('/{name}', handle)])
# if __name__ == '__main__':
# web.run_app(app, port=8000)




async def asyncWhile():
    while True:
        pass
    await a()