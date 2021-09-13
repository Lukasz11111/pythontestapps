#!/usr/bin/env python

import revdebug

import socket
import sys

revdebug.flush()  # force first AppState packets to be sent so recording is not deleted

def func(): pass

class cls:
    def meth(self): pass

    @classmethod
    def cmeth(cls): pass

    @staticmethod
    def smeth(): pass

    @property
    def prop(): pass


inst = cls()
# fp   = open(sys.argv[0])
# sock = socket.socket()

# sock.connect(('127.0.0.1', 5000))

objs = (
        None,
        Ellipsis,
        True,
        False,

        'Szczęście = 无知, \u0380',
        'Szczęście = 无知, \u0380'.encode('utf8'),
        bytearray('Szczęście = 无知, \u0380'.encode('utf8')),
        ''.join(chr(i) for i in range(160)),
        bytes(range(160)),
        bytearray(range(160)),

        0,
        1,
        -1,
        10000,
        1000000000,
        0x3fffffff,
        -0x3fffffff,
        0x40000000,
        10000000000,
        (0x3fffffff << 30) + 0x3fffffff,
        (0x3fffffff << 30) + 0x40000000,
        -((0x3fffffff << 30) + 0x40000000),
        1 << (30 * 29),
        1 << (30 * 0x100),

        1.0,
        1 / 5,
        1 / 7,
        float('inf'),
        float('-inf'),
        float('nan'),
        float('-nan'),
        1j,
        1j / 5,
        1j / 7,
        1.0,
        1+1j,
        float('inf') + 1j,
        float('-inf') - 1j,
        float('inf') * 1j,
        float('-inf') * 1j,
        float('inf') * 1j * 1j,
        float('-inf') * 1j * 1j,

        (),
        (1,),
        (1, 2),
        tuple(range(80)),
        frozenset({}),
        frozenset({1}),
        frozenset({1, 2}),
        frozenset(range(80)),

        func,
        cls,
        cls.meth,
        cls.cmeth,
        cls.smeth,
        cls.prop,
        inst,
        inst.meth,
        inst.cmeth,
        inst.smeth,

        bytearray,

        socket,
        sys,
        revdebug,
        ValueError('value_error'),
        RuntimeError,
        RuntimeError('runtime_error'),

        [1, 2, 3],
        {1:2, 3:4, 5:6},
        {1, 2, 3},
        list(range(80)),
        {i: str(i) for i in range(80)},
        set(range(80)),
        ((1, 2, 3), [1, 2, 3], {1:2, 3:4, 5:6}, {1, 2, 3}),
        [(1, 2, 3), [1, 2, 3], {1:2, 3:4, 5:6}, {1, 2, 3}],
        {1: ((1, 2, 3), [1, 2, 3], {1:2, 3:4, 5:6}, {1, 2, 3})},
        {(1, 2, 3), frozenset({1, 2, 3})},
        frozenset({(1, 2, 3), frozenset({1, 2, 3})}),

        # fp,
        # sock,
        )

print()
for i in objs:
    s = 'py: ' + repr(i) + '\nmy: ' + revdebug.stringify(i, 1).decode("utf-8") + '\n'
    print(s)

# sock.close()
# fp.close()

# revdebug.dump()
raise RuntimeError('done')
