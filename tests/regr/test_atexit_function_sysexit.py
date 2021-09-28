#!/usr/bin/env python

import sys

def f():
    sys.exit()

import atexit
atexit.register(f())

print("bye")

raise "You shall not pass"

