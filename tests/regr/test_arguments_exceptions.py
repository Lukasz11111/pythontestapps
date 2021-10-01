import sys
from types import TracebackType 

revdebug.setrecmode(revdebug.Crash)
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

try:
    p="before 2"
    revdebug.exception(ValueError, "You shall not pass!","")
except:
    p="after 2"

try:
    p="before 2"
    revdebug.exception(ValueError, "You shall not pass!")
except:
    p="after 2"


# raise "You shall not pass!"
print("END")