#!/usr/bin/env python

import asyncio
import psycopg
import os
import random
import string

HOST=os.getenv('DB_TEST_HOST') 
USER=os.getenv('DB_TEST_USER') 
PASS=os.getenv('DB_TEST_PASS') 
DB=os.getenv('DB_TEST_DB') 
PORT=os.getenv('DB_TEST_PORT')


async def a():
    async with await psycopg.AsyncConnection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as aconn:
        async with aconn.cursor() as acur:
            async with await psycopg.AsyncConnection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as aconn:
                async with aconn.cursor() as acur:
                    sql = f'''select * from public.user'''
                    await acur.execute(sql)
                    print(await acur.fetchall())


try:
    asyncio.run(a())
except:
    print("No this time")











