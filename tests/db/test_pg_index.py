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


async def main():
    async with await psycopg.AsyncConnection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as aconn:
        async with aconn.cursor() as acur:
            sql = f'''CREATE UNIQUE INDEX {''.join(random.choices(string.ascii_uppercase, k=12))} ON public.user (id);'''

            await acur.execute(sql)

async def mainerr():
    async with await psycopg.AsyncConnection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as aconn:
        async with aconn.cursor() as acur:
            sql = f'''CREATE UNIQUE INDEX {''.join(random.choices(string.ascii_uppercase, k=12))} ON public.user (name);'''

            await acur.execute(sql)          

asyncio.run(main())
asyncio.run(mainerr())

