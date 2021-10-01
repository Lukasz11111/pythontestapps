import math
test = math.inf

revdebug.setrecmode(revdebug.Crash)

try:
    revdebug.setrecmode(4)
except:
    print("err in int")
revdebug.snapshot("int")
try:
    revdebug.setrecmode(test)
except:
    print("err in inf")
revdebug.snapshot("inf")
try:
    revdebug.setrecmode(-100)
except:
    print("err in negativ number")
revdebug.snapshot("negativ number")
try:
    revdebug.setrecmode(100)
except:
    print("err in out of range")
revdebug.snapshot("out of range")
try:
    revdebug.setrecmode(0.1)
except:
    print("err in float")
revdebug.snapshot("float")
try:
    revdebug.setrecmode(5-1)
except:
    print("err in math operation")
revdebug.snapshot("math operation")
try:
    revdebug.setrecmode(None)
except:
    print("err in None")
revdebug.snapshot("None")
try:
    revdebug.setrecmode("1")
except:
    print("err in String")
revdebug.snapshot("String")
try:
    revdebug.setrecmode(revdebug.setrecmode(revdebug.setrecmode(revdebug.setrecmode(revdebug.Crash))))
except:
    print("err in nesting")
revdebug.snapshot("nesting")


