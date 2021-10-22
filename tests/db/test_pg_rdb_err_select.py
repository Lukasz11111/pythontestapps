from sshtunnel import SSHTunnelForwarder

import time
import os
import sys
import json
import psycopg2
from datetime import datetime



HOST="20.188.58.169"
PROTOCOL="http"

DBNAME="revdebug_db"
USER="rdb_user"  
PASSWORD="masterkey"

SSH_PKEY="tests/db/rdb_demo"

PORT=5432

DB_HOST="172.29.0.4"
KEY_PW="azureuser"

StartTime=1634751204
def singleOperation(query):
    with SSHTunnelForwarder(
            (HOST, 22),
            ssh_private_key=SSH_PKEY,
            ### in my case, I used a password instead of a private key
            ssh_username=KEY_PW,
        #  ssh_password="<mypasswd>", 
            local_bind_address=('0.0.0.0', 10022),
            remote_bind_address=(DB_HOST, 5432)) as server:
            
            server.start()    

            params = {
                'database': DBNAME,
                'user': USER,
                'password': PASSWORD,
                'host': 'localhost',
                'port': server.local_bind_port
                }

            conn = psycopg2.connect(**params)
            curs = conn.cursor()
            curs.execute(query)
            result = curs.fetchall()
            curs.close()
        
            return result[0][0]

def getREC():
    
    EndTime = time.time()
    EndTime=datetime.fromtimestamp(EndTime)
    result = singleOperation(f'''(SELECT COUNT(*) FROM public."Recordings"  WHERE "Created" >= '{StartTime}'::timestamp  and "Created" <=  '{EndTime});''')     
    return result



resultRecording = getREC()



print(f'Recording: {resultRecording}')
