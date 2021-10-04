import sys
from types import TracebackType 

revdebug.setrecmode(revdebug.Crash)

try:
    i = 1 / 0

except:
    exc_info = sys.exc_info()
    print(exc_info[0])

revdebug.exception(ValueError, ImportError("You shall not pass!"), exc_info[2])

# try:
#     p="before 1"
#     revdebug.exception(ValueError, "You shall not pass!", sys.exc_info())
# except:
#     p="after 1"

# try:
#     a= TracebackType
#     # revdebug.recrepr(a, str)
#     p="before 2"
#     revdebug.exception("ValueError", "You shall not pass!", a)
# except:
#     p="after 2"

# try:
#     p="before 2"
#     revdebug.exception("str", "You shall not pass!", sys.exc_info())
# except:
#     p="after 2"

# try:
#     p="before 2"
#     revdebug.exception(ValueError, "You shall not pass!","")
# except:
#     p="after 2"

# try:
#     p="before 2"
#     revdebug.exception(ValueError, "You shall not pass!")
# except:
#     p="after 2"


# raise "You shall not pass!"
print("END")