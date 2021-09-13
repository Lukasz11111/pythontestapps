#!/usr/bin/env python

import revdebug

from threading import Thread

revdebug.flush()

# memoryview

m = memoryview(b'123')
s = repr(m)

m.release()

m = m
s = repr(m)

# file IO

f = open('/dev/null')
s = repr(f)
f.close()

f = open('/dev/null', 'rb')
s = repr(f)
f.close()

# TODO: more extensive tests

# Thread

class MyThread2(Thread):
    def __init__(self, *args, **kwargs):
        return Thread.__init__(self, *args, **kwargs)

class MyThread3(MyThread2):
    pass

class MyThread4(Thread):
    __recrepr__ = False

class MyThread5(Thread):
    __recrepr__ = None

thread = Thread()
s = repr(thread)

mythread2 = MyThread2()
s = repr(mythread2)

mythread3 = MyThread3()
s = repr(mythread3)

mythread4 = MyThread4()
s = repr(mythread4)

mythread5 = MyThread5()
s = repr(mythread5)

# sockets

@revdebug.norecord
def _import():
    global _socket, socket
    from _socket import socket as _socket
    from socket import socket as socket

_import()

s = _socket()
t = repr(s)
s.close()

s = socket()
t = repr(s)
s.close()

revdebug.flush()  # force mode update

if revdebug.conn.mode == revdebug.Crash:
    raise RuntimeError('done')
