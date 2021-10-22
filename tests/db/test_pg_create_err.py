#!/usr/bin/env python

import asyncio
import psycopg


import os

HOST=os.getenv('DB_TEST_HOST') 
USER=os.getenv('DB_TEST_USER') 
PASS=os.getenv('DB_TEST_PASS') 
DB=os.getenv('DB_TEST_DB') 
PORT=os.getenv('DB_TEST_PORT')



async def create():
    async with await psycopg.AsyncConnection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as aconn:
        async with aconn.cursor() as acur:
            sql = '''CREATE TABLE accountserr (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
        last_login TIMESTAMP 
);'''

            await acur.execute(sql, ("root",))
            print(await acur.fetchall())

            await acur.executemany(sql, (("root",), ("root",)))
            print(await acur.fetchall())

            async for res in acur.stream(sql, ("root",)):
                print(res)

asyncio.run(create())
