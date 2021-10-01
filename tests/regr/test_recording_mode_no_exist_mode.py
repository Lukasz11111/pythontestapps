#!/usr/bin/env python

from time import sleep

i = 1

revdebug.setrecmode(12)
sleep(0.05)

i = 2
revdebug.exception(ValueError('2'))

