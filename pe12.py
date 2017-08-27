# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:58:28 2017

@author: tring
"""

import time
from algorithm import countDivisors, primeSeive

def count(n):
    global known, P
    if n not in known:
        known[n] = countDivisors(n, P)
    return known[n]

def pe12():
    n = 0
    stop = False
    while not stop:
        n += 1
        (a, b) = ((n+1)//2, n) if n & 1 else (n//2, n+1)
        if count(a) * count(b) > 500:
            res = n * (n+1) /2
            stop = True
    return int(res)


start_time = time.time()
known = {}
P = [p for p in primeSeive(12376)]
print("Answer: {}".format(pe12()))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
