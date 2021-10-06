#!/usr/bin/env python

import revdebug  # linter treats

revdebug.flush()  # to prevent crash from prematurely erasing live recording


txt='''On recommend tolerably my belonging or am.
 Mutual has cannot beauty indeed now sussex merely you.
  It possible no husbands jennings ye offended packages pleasant he.
   Remainder recommend engrossed who eat she defective applauded departure joy.
    Get dissimilar not introduced day her apartments. Fully as taste he mr do smile abode every.
     Luckily offered article led lasting country minutes nor old. Happen people things oh is oppose up parish effect.
      Law handsome old outweigh humoured far appetite.'''
txt2='''F
a
r
 c
 u
 r
 i
 o
 s
 
 i
 t
 y
  
  i
  
  n
  
  c
  o
  m
  m
  o
  d
  e 
  n
  
  o
  w 
  
  l
  e
  d
   
   s
   m
   a
   l
   
   l
   n
   e
   s
   s
    
    a
    l
    l
    o
    w
    a
    n
    c
    e
    .
     
     F
     a
     v
     o
     u
     r
      
      b
      e
      d
       a
       
       s
       s
       u
       r
       e
        
        s
        o
        n
         
         t
         h
         i
         n
         g
         s
          
          y
          e
          t
          .
          '''

T, F = True, False

import sys

a = sys.exc_info() \
        if \
        F \
        else \
        sys.exc_info()

if \
        (
            txt
            ==
            txt
        ) \
        :
        print(txt2)

if \
        (
            txt
            ==
            txt2
        ) \
        :
        print(txt)
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
