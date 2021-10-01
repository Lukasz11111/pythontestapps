import json
import os

os.chmod("test_permissions.txt", 0o777)

f = open('test_permissions.txt',)

print(f.readlines())
 
# Closing file
f.close()

os.chmod("test_permissions.txt", 0o000)


raise RuntimeError('done')

 

