import subprocess
from flask import Flask

revdebug.setrecmode(revdebug.Live)
revdebug.flush()  # compensating for live recording deletion on server

bashCmd = ["pip", "uninstall", "flask", "-y"]
process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
output, error = process.communicate()

# bashCmd = ["sdfdsf"]
# process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
# output, error = process.communicate()

