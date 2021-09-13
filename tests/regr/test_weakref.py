#!/usr/bin/env python

import revdebug

import weakref

def func():
    pass

class cls:
    pass


def test_start():
    inst = cls()

    r = weakref.ref(func)
    s = repr(r)

    r = weakref.ref(cls)
    s = repr(r)

    r = weakref.ref(inst)
    s = repr(r)

    r = weakref.ref(revdebug)
    s = repr(r)

    r = weakref.ref(weakref)
    s = repr(r)

    p = weakref.proxy(func)
    s = repr(p)

    p = weakref.proxy(cls)
    s = repr(p)

    p = weakref.proxy(inst)
    s = repr(p)

    p = weakref.proxy(revdebug)
    s = repr(p)

    p = weakref.proxy(weakref)
    s = repr(p)

    revdebug.flush()  # force mode update

    if revdebug.conn.mode == revdebug.Crash:
        raise RuntimeError('done')
