import json
import os

os.chmod("tests/regr/test_permissions.txt", 0o777)

f = open('tests/regr/test_permissions.txt',)

print(f.readlines())
 
# Closing file
f.close()

os.chmod("tests/regr/test_permissions.txt", 0o000)

if revdebug.conn.mode == revdebug.Crash:
    raise RuntimeError('done')

 


