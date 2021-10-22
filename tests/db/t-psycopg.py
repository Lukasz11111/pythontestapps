#!/usr/bin/env python

from skywalking import agent
agent.start()

import asyncio
import psycopg

# with psycopg.connect('postgresql://root:root@localhost:15432/admin') as conn:
with psycopg.Connection.connect('postgresql://root:root@localhost:5432/admin') as conn:
    with conn.cursor() as cur:
        sql = "select * from user where user = %s"

        cur.execute(sql, ("root",))
        print(cur.fetchall())

        cur.executemany(sql, (("root",), ("root",)))
        print(cur.fetchall())

        for res in cur.stream(sql, ("root",)):
            print(res)

async def main():
    async with await psycopg.AsyncConnection.connect('postgresql://root:root@localhost:5432/admin') as aconn:
        async with aconn.cursor() as acur:
            sql = "select * from user where user = %s"

            await acur.execute(sql, ("root",))
            print(await acur.fetchall())

            await acur.executemany(sql, (("root",), ("root",)))
            print(await acur.fetchall())

            async for res in acur.stream(sql, ("root",)):
                print(res)

asyncio.run(main())

from time import sleep; sleep(1)  # BUG? Agent is supposed to flush pending segments on exit so this should not be needed, but it is.
