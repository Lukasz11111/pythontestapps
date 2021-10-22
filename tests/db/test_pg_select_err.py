#!/usr/bin/env python

import asyncio
import psycopg

import os

HOST=os.getenv('DB_TEST_HOST') 
USER=os.getenv('DB_TEST_USER') 
PASS=os.getenv('DB_TEST_PASS') 
DB=os.getenv('DB_TEST_DB') 
PORT=os.getenv('DB_TEST_PORT')



def select():
    with psycopg.Connection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as conn:
        with conn.cursor() as cur:
            sql = '''select * from userd'''

            cur.execute(sql)
            print(cur.fetchall())

            # cur.executemany(sql, (("root",), ("root",)))
            # print(cur.fetchall())

            # for res in cur.stream(sql, ("root",)):
            #     print(res)

async def selectAsync():
    async with await psycopg.AsyncConnection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as aconn:
        async with aconn.cursor() as acur:
            sql = '''select * from userd'''

            await acur.execute(sql)
            print(await acur.fetchall())

            # await acur.executemany(sql, (("root",), ("root",)))
            # print(await acur.fetchall())

            # async for res in acur.stream(sql, ("root",)):
            #     print(res)

select()
asyncio.run(selectAsync())

raise "you shall not pass"

