#!/usr/bin/env python

import asyncio
import psycopg
import os

HOST=os.getenv('DB_TEST_HOST') 
USER=os.getenv('DB_TEST_USER') 
PASS=os.getenv('DB_TEST_PASS') 
DB=os.getenv('DB_TEST_DB') 
PORT=os.getenv('DB_TEST_PORT')



with psycopg.Connection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as conn:
    with conn.cursor() as cur:
        sql = "select * from public.user"

        cur.execute(sql)
        print(cur.fetchall())

        cur.executemany(sql, (("root",), ("root",)))
        print(cur.fetchall())

        for res in cur.stream(sql, ("root",)):
            print(res)

async def main():
    with psycopg.Connection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as conn:
        async with aconn.cursor() as acur:
            sql = "select * from user where user = %s"

            await acur.execute(sql, ("root",))
            print(await acur.fetchall())

            await acur.executemany(sql, (("root",), ("root",)))
            print(await acur.fetchall())

            async for res in acur.stream(sql, ("root",)):
                print(res)

asyncio.run(main())


