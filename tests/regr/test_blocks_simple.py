#!/usr/bin/env python

import asyncio as aio
import time


async def func1():
    async def func2():
        async def func3():
            i = 3
            await aio.sleep(0.06)
            i = 6
            print("func3")
            revdebug.block(False)
            revdebug.snapshot("func3")
        i = 2
        await aio.sleep(0.06)
        i = 5
        await func3()     
    i = 1
    await aio.sleep(0.06)
    i = 4
    revdebug.snapshot("func3")
    await func2()

        

async def main1():
    t1 = aio.create_task(func1())
    await aio.sleep(0.02)


    await aio.gather(t1)

    revdebug.flush()

aio.run(main1())