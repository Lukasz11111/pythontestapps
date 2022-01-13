import asyncio as aio


async def a():
    # revdebug.block()
    for i in range(0,10):
        print(i)
        await aio.sleep(1)
        # revdebug.snapshot(str(i))

aio.run(a())
