import subprocess
from flask import Flask
bashCmd = ["pip", "uninstall", "flask", "-y"]
process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
output, error = process.communicate()

# bashCmd = ["sdfdsf"]
# process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
# output, error = process.communicate()

