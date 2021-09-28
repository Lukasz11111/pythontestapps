#!/usr/bin/env python

import revdebug

import threading
import time

revdebug.flush()  # force first AppState packets to be sent so recording is not deleted

def thread_function():
    f()

import sys

def f():
    def g():
        print('thread exit')
        sys.exit()

    g()

def atexit_func():
    print('after exit')

import atexit
atexit.register(atexit_func)

threading.Thread(target = thread_function).start()

time.sleep(10)

raise RuntimeError('done')


