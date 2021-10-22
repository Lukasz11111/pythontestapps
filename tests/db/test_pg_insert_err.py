
#!/usr/bin/env python

import asyncio
import psycopg
import random
import os

HOST=os.getenv('DB_TEST_HOST') 
USER=os.getenv('DB_TEST_USER') 
PASS=os.getenv('DB_TEST_PASS') 
DB=os.getenv('DB_TEST_DB') 
PORT=os.getenv('DB_TEST_PORT')



async def insertAsync(x):
    async with await psycopg.AsyncConnection.connect(f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}') as aconn:
        async with aconn.cursor() as acur:
            await acur.execute(f'''INSERT INTO public.user (id, name) VALUES ('{x}sdf', 'sdf') ;''')
            


for x in range(0,10):
    try:
        z =random.randrange(1000,10000000000)
        asyncio.run(insertAsync(z))   
    except:
        print("err")


raise "you shall not pass"
