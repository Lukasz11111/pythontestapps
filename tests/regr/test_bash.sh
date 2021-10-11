python - << EOF
revdebug.setrecmode(revdebug.Live)
revdebug.flush()  
myPyString = "Do something on python"
#print(myPyString)
raise "You shall not pass!"
EOF