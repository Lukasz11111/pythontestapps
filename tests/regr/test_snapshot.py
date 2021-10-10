#!/usr/bin/env python

import threading
import time

import revdebug

def thread_func():
    revdebug.snapshot()

    time.sleep(0.1)

    revdebug.snapshotall()

@revdebug.norecord
def thread_wrapper(thread):  # create determinism
    thread.start()
    thread.join()

revdebug.flush()
revdebug.snapshot('“:♡.•♬✧⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾*+:•*∴')
revdebug.snapshot('o͡͡͡͡͡͡͡͡͡͡͡͡͡͡╮(｡❛ᴗ❛｡)╭o͡͡͡͡͡͡͡͡͡͡͡͡͡͡')
revdebug.snapshot('( ❀⃙⃕⃠⃝⃘⃚౪❀⃙⃕⃠⃝⃘⃚ )')
revdebug.snapshot('▒▒▓█▇▅▂∩( ✧Д✧)∩▂▅▇█▓▒▒')

thread = threading.Thread(target = thread_func, args = ())

time.sleep(0.1)

revdebug.snapshot()

time.sleep(0.1)

thread_wrapper(thread)

time.sleep(0.2)

if revdebug.conn.mode == revdebug.Crash:
    raise RuntimeError('done')
