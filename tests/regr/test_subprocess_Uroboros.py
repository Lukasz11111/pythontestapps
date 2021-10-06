
import subprocess
import time

# time.sleep(1)
print("Go next")

revdebug.setrecmode(revdebug.Crash)
revdebug.flush()  # compensating for live recording deletion on server

subprocess.check_call(['python','/app/tests/regr/test_subprocess_Uroboros.py', "err"])

raise "You shall not pass"