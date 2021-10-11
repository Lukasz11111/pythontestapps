#!/usr/bin/env python

import threading
import time


def thread_function():
    print("Start")
    for x in range(1,10):
        time.sleep(60)
    raise "You shall not pass!"



threading.Thread(target = thread_function).start()

time.sleep(0.1)

raise RuntimeError('done')