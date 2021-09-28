#!/usr/bin/env python

try:
    revdebug.setrecmode(revdebug.Live)

    revdebug.flush()  # to prevent crash from prematurely erasing live recording

    import time

    def atexit_func1():
        print('Last but not least')
        time.sleep(5)
        raise RuntimeError('1')

    def atexit_func2():
        print('I\'m go second')
        time.sleep(5)
        raise RuntimeError('2')

    def atexit_func3():
        print('I\'m go first')
        time.sleep(5)
        raise RuntimeError('3')

    import atexit

    atexit.register(atexit_func1)
    atexit.register(atexit_func2)
    atexit.register(atexit_func3)

    raise RuntimeError('3 2 1')
finally:
    revdebug.setrecmode(revdebug.Crash)