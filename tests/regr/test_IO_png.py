#!/usr/bin/env python

import revdebug

revdebug.flush()

# file IO

f = open('tests/regr/test.png')
s = repr(f)
f.close()

print(s)

f = open('tests/regr/test.png', "rb")

print(f.read())

if revdebug.conn.mode == revdebug.Crash:
    raise RuntimeError('done')
