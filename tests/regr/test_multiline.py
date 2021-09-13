#!/usr/bin/env python

import revdebug  # linter treats

revdebug.flush()  # to prevent crash from prematurely erasing live recording

T, F = True, False

import sys

a = sys.exc_info() \
        if \
        F \
        else \
        sys.exc_info()

if \
        not \
        (
        (
        (a
        :=
        1
        )
        and
        (
        b
        :=
        0
        )
        )
        or
        (
        (
        c
        :=
        0
        )
        or
        (
        d
        :=
        1
        )
        )
        ) \
        :
    d = 1

assert \
    (
    T
    ) \
    if \
    F \
    else \
    (
    T
    )

assert (
    T
    ) \
    and \
    (
    (
    (
    F
    )
    if
    (
    T
    )
    else
    (
    F
    )
    )
    or
    (
    T
    )
    )

if \
        F \
        or \
        T \
        :
    pass

if \
        (
        F
        or
        T
        ) \
        :
    pass

l = [
    i
    for
    i
    in
    range(5)
    if
    i
    &
    1
    if
    i
    >
    1
    ]

try:
    try:
        raise ValueError('value error')
    except \
            ValueError \
            as \
            exc \
            :
        b = exc
        raise
except \
        (
        TypeError,
        ValueError
        ) \
        as \
        exc \
        :
    b = exc
    raise


def \
        func(a =
        1):
    pass

func \
    (
        a
        =
        3
    )

class \
        cls \
        :
    pass

class \
    subcls \
        (
            cls
        ) \
        :
    pass

(
    lambda
    x
    :
    x**2
) \
(
    2
)

l = \
    [
    i
    for
    i
    in
    range
    (
    3
    )
    ]

raise RuntimeError('done')
