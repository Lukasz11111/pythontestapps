#!/usr/bin/env python

import revdebug
import os

try:  # OverflowError
    f = 100.0 ** 1000300000000.0
except:
    pass

try:  # ZeroDivisionError
    i = 1 / 0
except:
    pass

try:  # AssertionError
    assert False, 'message'
except:
    pass

try:  # AttributeError
    i = revdebug.nonexistent_attribute
except:
    pass

try:  # BufferError
    b = bytearray(b'0123452678')
    m = memoryview(b)
    del b[1]
except:
    del b, m

# TODO: EOFError

try:  # ModuleNotFoundError (ImportError)
    import nonexistent_module
except:
    pass

try:  # IndexError (LookupError)
    i = [1][2]
except:
    pass

try:  # KeyError (LookupError)
    try:
        i = {1: 2}['a']
    except:
        raise
except:
    pass

try:  # MemoryError
    b = bytearray(0x1000000000000000)
except:
    pass

try:  # UnboundLocalError
    def func():
        x += 1
    func()
except:
    pass

# OSError

try:
    f = open('nonexistent_file')
except:
    pass

try:
    os.rename('nonexistent_file', 'another_nonexistent_file')
except:
    pass

# TODO: ReferenceError

try:  # SyntaxError
    try:
        c = compile('i = [1, 2,', 'dir/filename.py', 'exec')
    except:
        raise
except:
    pass

try:  # IndentationError(SyntaxError)
    try:
        c = compile('def f():\ni = 1', 'dir/filename.py', 'exec')
    except:
        raise
except:
    pass

try:  # TabError(IndentationError(SyntaxError))
    try:
        c = compile('def f():\n i = 1\n\tj = 2', 'dir/filename.py', 'exec')
    except:
        raise
except:
    pass

try:  # TypeError
    s = frozenset({[1, 2, 3]})
except:
    pass

try:  # ValueError
    b = bytearray(-1)
except:
    pass

revdebug.flush()  # force mode update

if revdebug.conn.mode == revdebug.Crash:
    raise RuntimeError('some abnormal termination')
