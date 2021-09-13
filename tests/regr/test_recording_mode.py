#!/usr/bin/env python

from time import sleep

i = 1

revdebug.setrecmode(revdebug.Off)
sleep(0.05)

i = 2
revdebug.exception(ValueError('2'))

revdebug.setrecmode(revdebug.Crash)

i = 3
revdebug.exception(ValueError('3'))
sleep(0.05)

revdebug.setrecmode(revdebug.Live)

i = 4
revdebug.exception(ValueError('4'))
sleep(0.05)

revdebug.setrecmode(revdebug.Crash)

i = 5
revdebug.exception(ValueError('5'))
sleep(0.05)

revdebug.setrecmode(revdebug.Off)
sleep(0.05)

i = 6
revdebug.exception(ValueError('6'))

revdebug.setrecmode(revdebug.Live)

i = 7
revdebug.exception(ValueError('7'))
sleep(0.05)
