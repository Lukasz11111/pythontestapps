#!/usr/bin/env python

from time import sleep

i = 1
for x in range(1,100):
    revdebug.setrecmode(revdebug.Crash)
revdebug.exception(ValueError('1'))  

for x in range(1,100):
    revdebug.setrecmode(revdebug.Live)
revdebug.exception(ValueError('2'))   

revdebug.setrecmode(revdebug.Crash)
sleep(0.5)
i = 2
revdebug.exception(ValueError('3'))