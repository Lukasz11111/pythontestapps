import subprocess

bashCmd = ["cp", "-r", "tests/regr/test_delete_me.py", "tests/regr/test_delete_me2.py"]
process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
output, error = process.communicate()

bashCmd = ["rm", "tests/regr/test_delete_me.py"]
process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
output, error = process.communicate()

bashCmd = ["mv", "tests/regr/test_delete_me2.py", "tests/regr/test_delete_me.py"]
process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
output, error = process.communicate()

raise "You shall not pass"
