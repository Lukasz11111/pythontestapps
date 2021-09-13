#!/usr/bin/env python

import revdebug  # linter kibble

revdebug.flush()  # force first AppState packets to be sent so recording is not deleted

_ = '____ custom user object serialization ____________________________________________________________________________________________'
@revdebug.norecord
class cls:
    def __init__(self, x = 1, y = 2):
        self.x = x
        self.y = y

    def __recrepr__(self):
        return f'<my object stringification x={self.x}, y={self.y}>'

cls_inst = cls(3, 4)

cls_inst.x = -1

i = cls_inst

class subcls(cls):
    pass

subcls_inst = subcls()

@revdebug.norecord
class cls1:
    pass

@revdebug.norecord
class cls2:
    __recrepr__ = str

@revdebug.norecord
class cls3:
    def __recrepr__(self):
        return f'<my object stringification at 0x{id(self):12x}>'

l = [cls1(), cls2(), cls3()]

i1, i2, i3 = l


_ = '.... dynamic set ............................................................................................'
prev = revdebug.recrepr(subcls, None)

i = subcls_inst
i = cls_inst

prev = revdebug.recrepr(subcls, prev)

i = subcls_inst

_ = '.... for foreign objects ............................................................................................'
from collections import OrderedDict

i = OrderedDict(((1, 2), (3, 4)))
i[1] = -2
i = i

prev = revdebug.recrepr(OrderedDict, str)

i = i
i[1] = -3
i = i

revdebug.recrepr(OrderedDict, prev)

i = i
i[1] = -4

_ = '.... also built-in objects ............................................................................................'
l = [1, 2, 3]
prev = revdebug.recrepr(list, lambda self: f'<list of {len(self)} objects>')
l = l
revdebug.recrepr(list, prev)
l = l

l = {1: 1, 2: 2, 3: 3}
prev = revdebug.recrepr(dict, lambda self: f'<dict of {len(self)} objects>')
l = l
revdebug.recrepr(dict, prev)
l = l

l = {1, 2, 3}
prev = revdebug.recrepr(set, lambda self: f'<set of {len(self)} objects>')
l = l
revdebug.recrepr(set, prev)
l = l

l = bytearray(b'123')
prev = revdebug.recrepr(bytearray, lambda self: f'<bytearray of {len(self)} bytes>')
l = l
revdebug.recrepr(bytearray, prev)
l = l

l = ([1], [2], [3])
prev = revdebug.recrepr(tuple, lambda self: f'<tuple of {len(self)} objects>')
l = l
revdebug.recrepr(tuple, prev)
l = l

_ = '.... user serialization not limited in size (within reason) ............................................................................................'
l = list(range(200))
prevl = revdebug.recrepr(list, str)
l = l
t = (l, l)  # but limited if contained in object without custom recrepr

prevt = revdebug.recrepr(tuple, str)  # which can be fixed easily
t = t

revdebug.recrepr(list, prevl)
revdebug.recrepr(tuple, prevt)

_ = '.... having fun ............................................................................................'
l = [1, 2, 3, 4]

# if someone is not looking, slip the followin line into code they will be revdebugging to ensure hours of fun
revdebug.recrepr(int, lambda self: str(self) if self != 3 else '-1')

l = [1, 2, 3, 4]



raise RuntimeError('done')
