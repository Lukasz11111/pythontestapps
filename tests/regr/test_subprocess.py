
import subprocess

revdebug.setrecmode(revdebug.Crash)
revdebug.flush()  # compensating for live recording deletion on server

subprocess.check_call(['python','/app/tests/regr/test_throw_err.py', "err"])

raise "You shall not pass"