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
            sql = f''' SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog' AND 
    schemaname != 'information_schema';'''

            await acur.execute(sql)
            print(await acur.fetchall())

async def b():
    async with await psycopg.AsyncConnection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as aconn:
        async with aconn.cursor() as acur:
            sql = f''';;;;;;;;;;;;;;;;;;;'''

            await acur.execute(sql)          
async def c():
    async with await psycopg.AsyncConnection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as aconn:
        async with aconn.cursor() as acur:
            sql = f''''''

            await acur.execute(sql)          

async def d():
    async with await psycopg.AsyncConnection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as aconn:
        async with aconn.cursor() as acur:
            sql = f'''\dt'''

            await acur.execute(sql)          

async def e():
    async with await psycopg.AsyncConnection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as aconn:
        async with aconn.cursor() as acur:
            sql = f'''drop'''

            await acur.execute(sql)          

async def f():
    async with await psycopg.AsyncConnection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as aconn:
        async with aconn.cursor() as acur:
            sql = f'''restart'''

            await acur.execute(sql)          



try:
    asyncio.run(a())
except:
    print("No this time")

try:
    asyncio.run(b())
except:
    print("No this time")
try:
    asyncio.run(c())
except:
    print("No this time")
try:
    asyncio.run(d())
except:
    print("No this time")
try:
    asyncio.run(e())
except:
    print("No this time")
try:
    asyncio.run(f())
except:
    print("No this time")









