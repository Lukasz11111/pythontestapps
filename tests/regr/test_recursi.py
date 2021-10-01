#!/usr/bin/env python

revdebug.flush()  # force first AppState packets to be sent so recording is not deleted

def f():
    g()

def g():
    f()

f()