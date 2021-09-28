#!/usr/bin/env python

import revdebug

import threading
import time

revdebug.flush()  # force first AppState packets to be sent so recording is not deleted

def thread_function():
    raise "You shall not pass!"



threading.Thread(target = thread_function).start()

time.sleep(0.1)

raise RuntimeError('done')
