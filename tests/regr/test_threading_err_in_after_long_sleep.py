#!/usr/bin/env python

import revdebug

import threading
import time

revdebug.flush()  # force first AppState packets to be sent so recording is not deleted

def thread_function():
    print("Start")
    for x in range(1,10):
        time.sleep(60)
    raise "You shall not pass!"



threading.Thread(target = thread_function).start()

time.sleep(0.1)

raise RuntimeError('done')
