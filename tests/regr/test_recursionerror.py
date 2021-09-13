#!/usr/bin/env python

revdebug.flush()  # force first AppState packets to be sent so recording is not deleted

@revdebug.norecord
def f():
    g()

@revdebug.norecord
def g():
    f()

f()
