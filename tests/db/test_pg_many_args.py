#!/usr/bin/env python

import asyncio
import psycopg
import os

HOST=os.getenv('DB_TEST_HOST') 
USER=os.getenv('DB_TEST_USER') 
PASS=os.getenv('DB_TEST_PASS') 
DB=os.getenv('DB_TEST_DB') 
PORT=os.getenv('DB_TEST_PORT')


# with psycopg.Connection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as conn:
#     with conn.cursor() as cur:
#         # sql = "select * from user where user = %s;"
#         sql = "select * from public.user where name = %s;"
#         cur.execute(sql, ("gogo",), binary=True)
#         print(cur.fetchall())

async def main():
    async with await psycopg.AsyncConnection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as aconn:
        async with aconn.cursor() as acur:
            sql = '''select * from public.user where name = %s;'''

            await acur.execute(sql, ("gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo""gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo","gogo"), binary=True)
            print(await acur.fetchall())

asyncio.run(main())

