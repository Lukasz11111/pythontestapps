#!/usr/bin/env python

import revdebug  # linter kibble

revdebug.flush()  # force first AppState packets to be sent so recording is not deleted

_ = '____ inheritance ____________________________________________________________________________________________'
class mylist(list):
    pass

i = mylist([1, 2, 3])
i[1] = -2

i = i

prev = revdebug.recrepr(mylist, lambda self: f'<list of {len(self)} objects>')
i = i

prev2 = revdebug.recrepr(mylist, None)
i = i

prev2 = revdebug.recrepr(mylist, False)
i = i

prev2 = revdebug.recrepr(mylist, prev)
i = i

class mylist2(mylist):
    pass

i = mylist2([1, 2, 3])
i[1] = -2

i = i

prev = revdebug.recrepr(mylist2, lambda self: f'<list of {len(self)} objects>')
i = i

prev2 = revdebug.recrepr(mylist2, None)
i = i

prev2 = revdebug.recrepr(mylist2, False)
i = i

prev2 = revdebug.recrepr(mylist2, prev)
i = i

class mylist3(mylist2):
    __recrepr__ = lambda self: f'<list of {len(self)} objects>'

i = mylist3([1, 2, 3])

class mylist4(mylist2):
    __recrepr__ = None

i = mylist4([1, 2, 3])

class mylist5(mylist2):
    __recrepr__ = False

i = mylist5([1, 2, 3])

_ = '____ from other builtin objects ____________________________________________________________________________________________'
class myset(set):
    pass

i = myset([1, 2, 3])
i.add(-2)

i = i

prev = revdebug.recrepr(myset, lambda self: f'<set of {len(self)} objects>')
i = i

prev2 = revdebug.recrepr(myset, None)
i = i

prev2 = revdebug.recrepr(myset, False)
i = i

prev2 = revdebug.recrepr(myset, prev)
i = i

class mytuple(tuple):
    pass

i = mytuple([1, 2, 3])

prev = revdebug.recrepr(mytuple, lambda self: f'<tuple of {len(self)} objects>')
i = i

prev2 = revdebug.recrepr(mytuple, None)
i = i

prev2 = revdebug.recrepr(mytuple, False)
i = i

prev2 = revdebug.recrepr(mytuple, prev)
i = i

class mydict(dict):
    pass

i = mydict([(1, 1), (2, 2), (3, 3)])
i[1] = -2

i = i

prev = revdebug.recrepr(mydict, lambda self: f'<dict of {len(self)} objects>')
i = i

prev2 = revdebug.recrepr(mydict, None)
i = i

prev2 = revdebug.recrepr(mydict, False)
i = i

prev2 = revdebug.recrepr(mydict, prev)
i = i

class myfrozenset(frozenset):
    pass

i = myfrozenset([1, 2, 3])

prev = revdebug.recrepr(myfrozenset, lambda self: f'<frozenset of {len(self)} objects>')
i = i

prev2 = revdebug.recrepr(myfrozenset, None)
i = i

prev2 = revdebug.recrepr(myfrozenset, False)
i = i

prev2 = revdebug.recrepr(myfrozenset, prev)
i = i

class mybytearray(bytearray):
    pass

i = mybytearray([1, 2, 3])
i[1] = 4

i = i

prev = revdebug.recrepr(mybytearray, lambda self: f'<bytearray of {len(self)} objects>')
i = i

prev2 = revdebug.recrepr(mybytearray, None)
i = i

prev2 = revdebug.recrepr(mybytearray, False)
i = i

prev2 = revdebug.recrepr(mybytearray, prev)
i = i

revdebug.flush()  # force mode update

if revdebug.conn.mode == revdebug.Crash:
    raise RuntimeError('done')
