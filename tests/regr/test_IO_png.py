#!/usr/bin/env python

import revdebug

revdebug.flush()

f = open('tests/regr/test.png', "rb")

print(f.read())

if revdebug.conn.mode == revdebug.Crash:
    raise RuntimeError('done')
