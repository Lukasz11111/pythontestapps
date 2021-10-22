#!/usr/bin/env python

import asyncio as aio
import time
import threading

def thread_function():
    time.sleep(5)
    a=0
    print("go next")
    aio.run(main1())
    # raise "You shall not pass"

async def func1():
    print("hello")
    threading.Thread(target = thread_function).start()
    await aio.sleep(0.02)
    threading.Thread(target = thread_function).start()


     

async def main1():
    t1 = aio.create_task(func1())
    await aio.sleep(0.02)

    await aio.gather(t1)



aio.run(main1())