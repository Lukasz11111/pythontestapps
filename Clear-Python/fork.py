#!/usr/bin/env python

import os
import time



if os.fork():
    print('parent')

else:
    time.sleep(0.2)

    print('child')


print("bye")