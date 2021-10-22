#!/usr/bin/env python

import asyncio
import psycopg

def select():
    with psycopg.Connection.connect('postgresql://rdb_user:masterkey@192.168.32.1:5432/revdebug_db') as conn:
        with conn.cursor() as cur:
            sql = '''select * from userd'''

            cur.execute(sql)
            print(cur.fetchall())


async def selectAsync():
    async with await psycopg.AsyncConnection.connect('postgresql://rdb_user:masterkey@192.168.32.1:5432/revdebug_db') as aconn:
        async with aconn.cursor() as acur:
            sql = '''select * from userd'''

            await acur.execute(sql)
            print(await acur.fetchall())



for x in range(0,100):
    try:
        select()
    except:
        print("err")
    try:
        asyncio.run(selectAsync())
    except:
        print("err")


raise "you shall not pass"

