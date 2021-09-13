#!/usr/bin/env python

import revdebug  # linter kibble

revdebug.flush()  # to prevent crash from prematurely erasing live recording

for iteration in range(3):
    _ = '____ store and delete ____________________________________________________________________________________________________________________________'

    a = 'store_name (is really store_local)'
    del a

    def func_store_del():
        global b

        b = 'store_global'
        del b

        c = 'store_fast'
        del c

        d = 'store_deref (closure var)'

        def closure():
            nonlocal d
            d += ' another_store_deref'
            del d

        return closure

    closure = func_store_del()
    closure()

    _ = '.... store / del subscript ............................................................................................'
    l = [1, 2, 3]

    l[1] = 'store_subscr'

    l[2:2] = ['store_subscr_slice', '...']

    del l[1]

    _ = '.... more store / del ............................................................................................'
    a = b = c = 1

    a += 1
    a *= 2
    a **= 3

    d = lambda: None
    d.b = 1

    d.a = l[2:2] = d.b = [4, 5, 6]

    del b, l[1], c
    del l[0:-1]
    del d.b, d.a

    e = [ # multi-line store
        int('1'),
        int('2'),
        int('3')
    ]

    _ = '.... class and attribute ............................................................................................'
    class cls:
        a = 'class_var'

        def method(self, a, *args, b = 'predefined_kw', **kwargs):
            return None

        @classmethod
        def cmethod(cls, *args, b = 'predefined_kw', **kwargs):
            return None

        @staticmethod
        def smethod(a, *args, b = 'predefined_kw', **kwargs):
            return None

    cls.b = 'another_class_var'

    inst = cls()

    inst.attr = 'store_attr'


    _ = '____ call function ____________________________________________________________________________________________________________________________'
    def func_call(a, *args, b = 'predefined_kw', **kwargs):
        return None

    func_call(1, 2, b = 4, c = 5)

    _ = '.... call method ............................................................................................'
    inst.method(1, 2, b = 4, c = 5)
    inst.cmethod(1)
    inst.smethod(1)

    _ = '.... complicated parameters ............................................................................................'
    import sys

    def fd_up(a, /, b, c, *args, d = 1, e = 2, f = 3, **kwargs):
        log = f'{a=}, {b=}, {c=}, {args=}, {d=}, {e=}, {f=}, {kwargs=}'

    fd_up(1, 2, *(3, 4), 5, d = 6, *(7,), **{'e': 8, 'g': 9}, f = 10, h = 11, **{'i': 12})
    fd_up(*range(2), *range(-1, -4, -1), **dict(zip('fgh', sys.exc_info())))


    _ = '____ lambdas, generators and comprehension ____________________________________________________________________________________________________________________________'
    lamb = lambda: 1

    a = lamb()

    a = (lambda: 2)()

    a = (lambda x, y: x + y)(1, 2)

    _ = '.... generator ............................................................................................'
    def generator():
        for i in range(3):
            yield i

    for a in generator():
        b = a

    _ = '.... yield from other generator ............................................................................................'
    def yield_from_other(x):
        yield from range(x, 0, -1)
        yield from range(x)

    for a in yield_from_other(3):
        b = a

    _ = '.... send to generator ............................................................................................'
    def double_inputs():
        while True:
            x = yield
            yield x * 2

    gen = double_inputs()

    next(gen)
    log = gen.send(10)

    _ = '.... comprehension ............................................................................................'
    l = [i for i in generator()]

    l = [i for i in range(3)]

    l = {i for i in range(3)}

    l = {i: str(i) for i in range(3)}

    l = (i for i in range(3))

    l = list(l)

    l = [i * j for i in range(3) for j in range(3)]


    _ = '____ flow control ____________________________________________________________________________________________________________________________'
    T, F = True, False

    if T:
        b = 'true'
    else:
        b = 'false'

    if not T:
        b = 'false'
    elif not not not T:
        b = 'also false'
    else:  # else does not generate any code so can not currently be mapped back to a line
        b = 'true'

    _ = '.... for loop ............................................................................................'
    for a in [1, 2, 3]:
        b = a

    _ = '.... while loop............................................................................................'
    while a < 6:
        a += 1

    while not a < 4:
        a -= 1

    _ = '.... continue, break and else ............................................................................................'
    for a in range(6):
        if a & 1:
            continue
        else:
            b = 2
        if a == 4:
            break
        b = a
    else:
        b = 'else'

    _ = '.... for else taken ............................................................................................'
    for a in range(3):
        pass
    else:
        b = 'else'

    _ = '.... messy single-line code ............................................................................................'
    for c in range(3): d = c
    else: d = 'else'

    _ = '.... if expression ............................................................................................'
    b = 1 if a else 2

    _ = '.... if filter ............................................................................................'
    l = [i for i in range(5) if i & 1]

    l = [i for i in range(5) if i & 1 if i > 1]

    _ = '.... compound conditionals ............................................................................................'
    assert (T > F) if T else (F < T)
    assert (T > F) if F else (F < T)

    assert (T) and (((F) if (T) else (F)) or (T))

    while T and ((F if T else F) or T):
        break

    if (T and F) or (F or T):
        pass

    if not ((T and F) or (F or T)):
        d = 1

    if not (((a := 1) and (b := 0)) or ((c := 0) or (d := 1))):
        d = 1

    _ = '.... special internally optimized expressions ............................................................................................'
    i = T and F or T
    i = (T and T) and T
    i = (F or F) or T
    i = (F or T) and T


    _ = '____ exceptions ____________________________________________________________________________________________________________________________'
    try:
        a = ((2 * 3) - (1 / 0)) + 5
    except:
        b = 'except'
    else:
        b = 'else'
    finally:  # finally does not generate any code so can not currently be mapped back to a line
        b = 'finally'

    _ = '................................................................................................'
    try:
        a = 1 / 2
    except:
        b = 'except'
    else:
        b = 'else'
    finally:
        b = 'finally'

    _ = '.... single line ............................................................................................'
    try: a = 1 / 0
    except: b = 'except'
    else: b = 'else'
    finally: b = 'finally'

    _ = '.... raise ............................................................................................'
    try:
        raise ValueError('value error')
    except ValueError as exc:
        b = exc

    _ = '.... nested re-raise ............................................................................................'
    def err_func():
        raise ValueError('value error')

    try:
        try:
            try:
                err_func()
            except ValueError:
                a = 1
                raise
        except ValueError:
            a = 2
            raise
    except ValueError:
        a = 3

    _ = '.... nested func ............................................................................................'
    def func(x, y):
        def inner_func():
            return x / y

        inner_func()

    try:
        b = func(1, 0)
    except ZeroDivisionError:
        b = 'zero division error'

    # THIS IS NOT DETERMINISTIC ENOUGH FOR TESTING!
    # _ = '.... signal unhandled exception ............................................................................................'
    # try:
    #     i = 1 / 0
    # except:
    #     revdebug.exception()

    # try:
    #     i = 1 / 0
    # except:
    #     e, v, tb = sys.exc_info()

    # revdebug.exception(e, v, tb)


    _ = '____ misc ____________________________________________________________________________________________________________________________'

    _ = '.... unicode ............................................................................................'
    Szczęście = "无知"

    _ = '.... context manager (nothing weird) ............................................................................................'
    import contextlib

    with contextlib.nullcontext() as c:
        b = 1

    _ = '.... annotations ............................................................................................'
    def f(a: str, b: str) -> str:
        return a + b

    f('1', '2')

    _ = '.... dynamic control of recording ............................................................................................'
    def func():
        a = 'func recorded'
        return 1

    func()
    revdebug.norecord(func)
    func()
    revdebug.record(func)
    func()

    _ = '.... overloaded operators (implicit functions) ............................................................................................'
    class cls:
        def __init__(self, val):
            self.val = val

        def __add__(self, other):
            return cls(self.val + other.val)

    # revdebug.norecord(cls.__init__)

    v0 = cls(0)
    v1 = cls(1)
    v2 = cls(2)
    v3 = cls(3)

    i = v1 + v2
    s = sum([v1, v2, v3], v0)


    _ = '____ custom user object serialization ____________________________________________________________________________________________'
    @revdebug.norecord
    class cls:
        def __init__(self, x = 1, y = 2):
            self.x = x
            self.y = y

        # This version of this function will cause an error when called for recording __init__(self, ...) since it does not
        # check if the class has already been initialized. This is intentional and will simply be recorded as a value of
        # *ERROR* until the class is fully initialized after __init__.
        def __recrepr__(self):
            return f'<my object stringification x={self.x}, y={self.y}>'

    i = cls(3, 4)

    i.x = -1

    j = i

    class subcls(cls):
        pass

    i = subcls()

    @revdebug.norecord
    class cls1:
        pass

    @revdebug.norecord
    class cls2:
        __recrepr__ = repr

    @revdebug.norecord
    class cls3:
        def __recrepr__(self):
            return f'<my object stringification at 0x{id(self):12x}>'

    l = [cls1(), cls2(), cls3()]

    i1, i2, i3 = l


    _ = '.... dynamic set ............................................................................................'
    prev = revdebug.recrepr(subcls, None)

    i = subcls()
    i = cls()

    prev = revdebug.recrepr(subcls, prev)

    i = subcls()

    _ = '.... for foreign objects ............................................................................................'
    from collections import OrderedDict

    i = OrderedDict(((1, 2), (3, 4)))
    i[1] = -2
    i = i

    prev = revdebug.recrepr(OrderedDict, OrderedDict.__repr__)  # this is a one-way system-wide operation and can never be changed back

    i = i
    i[1] = -3
    i = i

    revdebug.recrepr(OrderedDict, prev)  # this is a one-way system-wide operation and can never be changed back

    i = i
    i[1] = -4

    _ = '.... also built-in objects ............................................................................................'
    l = [1, 2, 3]
    prev = revdebug.recrepr(list, lambda self: f'<list of {len(self)} objects>')
    l = l
    prev = revdebug.recrepr(list, prev)
    l = l

    l = {1: 1, 2: 2, 3: 3}
    prev = revdebug.recrepr(dict, lambda self: f'<dict of {len(self)} objects>')
    l = l
    prev = revdebug.recrepr(dict, prev)
    l = l

    l = {1, 2, 3}
    prev = revdebug.recrepr(set, lambda self: f'<set of {len(self)} objects>')
    l = l
    prev = revdebug.recrepr(set, prev)
    l = l

    l = bytearray(b'123')
    prev = revdebug.recrepr(bytearray, lambda self: f'<bytearray of {len(self)} objects>')
    l = l
    prev = revdebug.recrepr(bytearray, prev)
    l = l

    l = ([1], [2], [3])
    prev = revdebug.recrepr(tuple, lambda self: f'<tuple of {len(self)} objects>')
    l = l
    prev = revdebug.recrepr(tuple, prev)
    l = l

    _ = '.... user serialization not limited in size (within reason) ............................................................................................'
    l = list(range(200))
    prev = revdebug.recrepr(list, list.__str__)
    l = l
    prev = revdebug.recrepr(list, prev)
    l = l


    _ = '____ async and coroutines (YIELD_FROM Future = AWAIT) ____________________________________________________________________________________________________________________________'
    import asyncio
    import time

    async def coroutine(delay, who):
        start = who + ' start: ' + time.strftime("%X")
        await asyncio.sleep(0)  # delay)
        end = who + ' end: ' + time.strftime("%X")

    async def main():
        await asyncio.gather(coroutine(0.1, 'alice'), coroutine(0.2, 'bob'))

    asyncio.run(main())

    _ = '.... async generator and for ............................................................................................'
    async def async_gen(delay, to):
        for i in range(to):
            await asyncio.sleep(0)  # delay)
            yield i

    async def main():
        asyncio.create_task(coroutine(0.1, 'charlie'))

        async for i in async_gen(0.2, 3):
            b = 'async for ' + str(i) + ' at: ' + time.strftime("%X")

    asyncio.run(main())


    _ = '____ decorators ____________________________________________________________________________________________'
    import functools

    def repeat(num_times):
        def decorator_repeat(func):
            @functools.wraps(func)
            def wrapper_repeat(*args, **kwargs):
                for _ in range(num_times):
                    value = func(*args, **kwargs)
                return value
            return wrapper_repeat
        return decorator_repeat

    def count_calls(func):
        @functools.wraps(func)
        def wrapper_count_calls(*args, **kwargs):
            wrapper_count_calls.num_calls += 1
            log = f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}"
            return func(*args, **kwargs)
        wrapper_count_calls.num_calls = 0
        return wrapper_count_calls

    revdebug.norecord(repeat)
    revdebug.norecord(count_calls)

    @repeat(num_times=3)
    @count_calls
    def say_whee(*args, **kwargs):
        log = "Whee!"

    say_whee()

    num_calls = say_whee.__wrapped__.num_calls

    _ = '.... record disable decorator ............................................................................................'
    @revdebug.norecord
    def func():
        log = 'This will not be recorded.'

    func()

    @revdebug.norecord
    class cls:
        def __init__(self):
            pass

        def func(self):
            pass

    i = cls()
    i.func()

    _ = '.... class decorator ............................................................................................'
    from dataclasses import dataclass

    @dataclass
    class PlayingCard:
        rank: str
        suit: str

    # redundant
    # _ = '.... class as decorator ............................................................................................'
    # class CountCalls:
    #     def __init__(self, func):
    #         functools.update_wrapper(self, func)
    #         self.func = func
    #         self.num_calls = 0

    #     def __call__(self, *args, **kwargs):
    #         self.num_calls += 1
    #         log = f"Call {self.num_calls} of {self.func.__name__!r}"
    #         return self.func(*args, **kwargs)

    # @CountCalls
    # def say_whee():
    #     log = Whee!"

    # say_whee()
    # say_whee()


    _ = '____ metaclasses ____________________________________________________________________________________________'
    class LittleMeta(type):
        def __new__(cls, clsname, superclasses, attributedict):
            attributedict['func3'] = cls.func3
            return type.__new__(cls, f'Meta{clsname}', superclasses, attributedict)

        def func3(self):
            pass

    class S:
        def func1(self):
            pass

    class A(S, metaclass=LittleMeta):
        def func2(self):
            pass

        def func3(self):
            pass

    a = A()
    i = A.func1
    i = A.func2
    i = A.func3

    _ = '.... subclass initializer ............................................................................................'
    class Philosopher:
        def __init_subclass__(cls, /, default_name, **kwargs):
            super().__init_subclass__(**kwargs)
            cls.default_name = default_name

    class AustralianPhilosopher(Philosopher, default_name="Bruce"):
        pass

    # non-deterministic
    # _ = '____ threads, each thread has its own ring buffer ____________________________________________________________________________________________________________________________'
    # import threading

    # log = '%s.%d: MAIN - START' % (time.strftime("%X"), time.time_ns())

    # def thread_function(name, count):
    #     log = '%s.%d: %s - START' % (time.strftime("%X"), time.time_ns(), name)

    #     for i in range(count):
    #         time.sleep(0.01)
    #         log = '%s.%d: %s - %d' % (time.strftime("%X"), time.time_ns(), name, i)

    #     log = '%s.%d: %s - END' % (time.strftime("%X"), time.time_ns(), name)

    #     # revdebug.dump()

    # threading.Thread(target = thread_function, args =('Alice %d' % iteration, 2)).start()
    # threading.Thread(target = thread_function, args =('Bob %d' % iteration, 3)).start()
    # threading.Thread(target = thread_function, args =('Charlie %d' % iteration, 4)).start()

    # time.sleep(0.01)  # let the threads tick once

    # log = '%s.%d: MAIN - END' % (time.strftime("%X"), time.time_ns())


_ = '.... dump main thread ring buffer ............................................................................................'
# revdebug.dump()

revdebug.flush()  # force mode update

if revdebug.conn.mode == revdebug.Crash:
    raise RuntimeError('done')
