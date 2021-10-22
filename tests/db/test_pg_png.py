#!/usr/bin/env python

import asyncio
import psycopg
import os
import random
import string
import sys

HOST=os.getenv('DB_TEST_HOST') 
USER=os.getenv('DB_TEST_USER') 
PASS=os.getenv('DB_TEST_PASS') 
DB=os.getenv('DB_TEST_DB') 
PORT=os.getenv('DB_TEST_PORT')

with open("tests/db/B.png", "rb") as image:
  f = image.read()
  b = bytearray(f)


async def a():
    async with await psycopg.AsyncConnection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as aconn:
        async with aconn.cursor() as acur:
                    sql = f'''INSERT INTO files(id, orig_filename, file_data) VALUES (DEFAULT,%s,%s) RETURNING id;'''
                    await acur.execute(sql,("nice", b))
                    print(await acur.fetchall())


def b():
    with psycopg.Connection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as conn:
        with conn.cursor() as cur:
            sql = '''INSERT INTO files(id, orig_filename, file_data) VALUES (DEFAULT,%s,%s) RETURNING id;'''

            cur.execute(sql,("nice", b))
            print(cur.fetchall())




try:
    asyncio.run(a())
except:
    print("No this time")
try:
    b()
except:
    print("No this time")



