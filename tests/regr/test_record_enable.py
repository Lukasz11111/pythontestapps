#!/usr/bin/env python

import revdebug  # linter medicine

_ = '.... code objects ............................................................................................'
def func():
    _ = 'func()'

func()
revdebug.norecord(func.__code__)
func()
revdebug.record(func.__code__)
func()


_ = '.... functions ............................................................................................'
revdebug.norecord(func)
func()
revdebug.record(func)
func()


_ = '.... classes ............................................................................................'
class cls:
    def __new__(cls):
        _ = 'cls.__new__()'
        return object.__new__(cls)

    def __init__(self):
        _ = 'cls.init()'

    def method(self):
        _ = 'cls.method()'

    @classmethod
    def classm(cls):
        _ = 'cls.classm()'

    @staticmethod
    def staticm():
        _ = 'cls.static()'

def func(self):
    _ = 'func()'

cls.func = func

_ = '....................................................................................'
inst = cls()
inst.method()
inst.classm()
inst.staticm()
inst.func()

revdebug.norecord(cls)

inst = cls()
inst.method()
inst.classm()
inst.staticm()
inst.func()

revdebug.record(cls.__new__)
revdebug.record(cls.__init__)
revdebug.record(cls.method)
revdebug.record(cls.staticm)
revdebug.record(cls.classm)
revdebug.record(cls.func)

inst = cls()
inst.method()
inst.classm()
inst.staticm()
inst.func()


# _ = '.... modules ............................................................................................'
import collections
import copy

copy.copy((1,))
collections.Counter()

revdebug.record(collections)
revdebug.record(copy)

copy.copy((1,))
collections.Counter()

revdebug.norecord(collections)
revdebug.norecord(copy)

copy.copy((1,))
collections.Counter()


_ = '.... filenames ............................................................................................'
revdebug.record(copy.__file__)
copy.copy((1,))
revdebug.norecord(copy.__file__)
copy.copy((1,))


_ = '.... paths ............................................................................................'

import os

path = os.path.dirname(copy.__file__)

revdebug.record(path)
copy.copy((1,))
revdebug.norecord(path)
copy.copy((1,))


# _ = '.... enable / disable currently executing code ............................................................................................'
def disable_self():
    revdebug.norecord(disable_self)
    return 'should be disabled'

disable_self()

@revdebug.norecord
def enable_self():
    revdebug.record(enable_self)
    return 'should be enabled'

enable_self()

_ = '....................................................................................'
def disable_parent():
    def disabled_child():
        revdebug.norecord(disable_parent)
        return 'should be disabled'

    return disabled_child()

disable_parent()

@revdebug.norecord
def enable_parent():
    def enabled_child():
        revdebug.record(enable_parent)
        return 'should be enabled'

    return enabled_child()

enable_parent()

_ = '....................................................................................'
def f1():
    i = 1
    revdebug.norecord(f5)
    revdebug.record(f4)
    revdebug.norecord(f3)
    revdebug.record(f2)
    revdebug.norecord(f1)
    return 1

@revdebug.norecord
def f2():
    i = 2
    f1()
    return 2

def f3():
    i = 3
    f2()
    return 3

@revdebug.norecord
def f4():
    i = 4
    f3()
    return 4

def f5():
    i = 5
    f4()
    return 5

f5()


_ = '.... dump main thread ............................................................................................'
revdebug.flush()  # force mode update

if revdebug.conn.mode == revdebug.Crash:
    raise RuntimeError('done')
