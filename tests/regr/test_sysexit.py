#!/usr/bin/env python

import sys

def f():
    def g():
        sys.exit()

    g()

def atexit_func():
    print('after exit')

import atexit
atexit.register(atexit_func)

f()
