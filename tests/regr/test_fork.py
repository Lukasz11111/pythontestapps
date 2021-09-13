#!/usr/bin/env python

import os
import time

import revdebug

if os.fork():
    print('parent')

else:
    time.sleep(0.2)

    print('child')
