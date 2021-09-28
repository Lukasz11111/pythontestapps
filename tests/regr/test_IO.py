#!/usr/bin/env python

import revdebug

revdebug.flush()

# file IO

f = open('tests/regr/test.txt')
s = repr(f)
f.close()

print(s)

f = open("tests/regr/test.txt", "r", encoding="utf-8")

print(f.readlines())

if revdebug.conn.mode == revdebug.Crash:
    raise RuntimeError('done')
