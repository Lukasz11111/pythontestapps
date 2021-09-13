#!/usr/bin/env python

import threading
import time

revdebug.flush()  # to prevent crash from prematurely erasing live recording

log = '%s.%d: MAIN - START' % (time.strftime("%X"), time.time_ns())

def thread_function(idx):
    log = '%s.%d: %d - START' % (time.strftime("%X"), time.time_ns(), idx)

    time.sleep(0.01)

    log = '%s.%d: %d - END' % (time.strftime("%X"), time.time_ns(), idx)

for i in range(16):
    thr = threading.Thread(target = thread_function, args = (i,), daemon = False).start()

log = '%s.%d: MAIN - END' % (time.strftime("%X"), time.time_ns())

# raise RuntimeError('done')
