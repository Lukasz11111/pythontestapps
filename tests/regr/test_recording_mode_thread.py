#!/usr/bin/env python

import revdebug 

import threading
import time

revdebug.flush()  # force first AppState packets to be sent so recording is not deleted

def thread_function():
    for i in range(1,100):
        revdebug.setrecmode(revdebug.Crash)
        time.sleep(0.01)
        revdebug.setrecmode(revdebug.Live)

def thread_function_err():
    for i in range(1,200):
        revdebug.exception(ValueError("You shall not pass!"))  

threading.Thread(target = thread_function).start()
threading.Thread(target = thread_function_err).start()



