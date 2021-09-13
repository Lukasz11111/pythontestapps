#!/usr/bin/env python

import asyncio as aio
from contextvars import copy_context
import time


async def func1():
    i = 1
    await aio.sleep(0.06)
    i = 4

async def func2():
    i = 2
    await aio.sleep(0.06)
    i = 5

async def func3():
    i = 3
    await aio.sleep(0.06)
    i = 6

async def main1():
    t1 = aio.create_task(func1())
    await aio.sleep(0.02)
    t2 = aio.create_task(func2())
    await aio.sleep(0.02)
    t3 = aio.create_task(func3())
    await aio.sleep(0.02)

    await aio.gather(t1, t2, t3)

    revdebug.flush()

aio.run(main1())


async def main2():
    revdebug.block()
    revdebug.snapshot('block 1')
    time.sleep(0.02)

    def func():
        revdebug.snapshot('block 2')
        time.sleep(0.02)

    copy_context().run(func)
    time.sleep(0.02)

aio.run(main2())

revdebug.snapshot('main')
time.sleep(0.02)


async def main3():
    async def func1(name):
        revdebug.snapshot(name)
        time.sleep(0.02)

    async def func2(name):
        revdebug.block()
        revdebug.snapshot(name)
        time.sleep(0.02)

    await func1('1')
    await aio.sleep(0.02)
    await aio.create_task(func1('2'))
    await aio.sleep(0.02)
    await aio.create_task(func2('3'))
    await aio.sleep(0.02)
    await func2('4')
    await aio.sleep(0.02)

    revdebug.snapshot('5')
    time.sleep(0.02)

aio.run(main3())

revdebug.snapshot('6')
time.sleep(0.02)


def func4(name):
    revdebug.block()
    revdebug.snapshot(name)
    time.sleep(0.02)

copy_context().run(func4, '7')

@revdebug.norecord
def func5():
    copy_context().run(func4, '8')

func5()

revdebug.snapshot('9')
time.sleep(0.02)
