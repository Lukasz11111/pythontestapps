#!/usr/bin/env python


try:
    revdebug.setrecmode(revdebug.Live)

    revdebug.flush()  # to prevent crash from prematurely erasing live recording

    import time

    def atexit_func():
        print('after exit')

        time.sleep(0.1)

        raise RuntimeError('abnormal stuff in atexit_func()')

    import atexit

    atexit.register(atexit_func)

    raise RuntimeError('some abnormal termination')
except:
    revdebug.setrecmode(revdebug.Crash)