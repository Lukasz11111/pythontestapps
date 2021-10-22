
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
        sql = "DELETE FROM  public.user"

        cur.execute(sql)
