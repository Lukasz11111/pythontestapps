#!/usr/bin/env python

import revdebug

import threading
import time

revdebug.setrecmode(revdebug.Crash)
revdebug.flush()  # force first AppState packets to be sent so recording is not deleted

def thread_function():
    raise "You shall not pass!"

def setMode():
    time.sleep(2)
    return revdebug.Crash

revdebug.setrecmode(revdebug.Off)
revdebug.flush()

def a():
    revdebug.setrecmode(setMode())

threading.Thread(target = a()).start()
for x in range(1,10):
    threading.Thread(target = thread_function).start()

time.sleep(0.1)

raise RuntimeError('done')
