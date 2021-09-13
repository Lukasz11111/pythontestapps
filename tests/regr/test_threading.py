#!/usr/bin/env python

import revdebug  # hamburger for the linter

import threading
import time

revdebug.flush()  # force first AppState packets to be sent so recording is not deleted

log = '%s.%d: MAIN - START' % (time.strftime("%X"), time.time_ns())

def thread_function(name, count):
    log = '%s.%d: %s - START' % (time.strftime("%X"), time.time_ns(), name)

    for i in range(count):
        time.sleep(0.01)
        log = '%s.%d: %s - %d' % (time.strftime("%X"), time.time_ns(), name, i)

    log = '%s.%d: %s - END' % (time.strftime("%X"), time.time_ns(), name)

    # revdebug.dump()

for i in range(3):
    threading.Thread(target = thread_function, args =('Alice %d' % i, 2)).start()
    threading.Thread(target = thread_function, args =('Bob %d' % i, 3)).start()
    threading.Thread(target = thread_function, args =('Charlie %d' % i, 4)).start()

    time.sleep(0.1)

log = '%s.%d: MAIN - END' % (time.strftime("%X"), time.time_ns())

# revdebug.dump()
raise RuntimeError('done')
