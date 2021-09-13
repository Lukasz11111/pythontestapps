#!/usr/bin/env python

import revdebug
import sys
import time

revdebug.flush()

try:
    i = 1 / 0

except:
    exc_info = sys.exc_info()

    revdebug.exception()

time.sleep(0.1)

revdebug.exception(*exc_info)
