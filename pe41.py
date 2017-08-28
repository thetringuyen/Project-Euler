# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:37:55 2017

@author: tring
"""
import time
from algorithm import isPrime
from itertools import permutations


def pe41():
    n = 9
    found = False
    res = -1
    while n > 0 and not found:
        p0 = ''.join([str(p) for p in range(1, n+1)])
        P = [int(''.join(p)) for p in permutations(p0)]
        P.sort(reverse=True)
        i = 0
        while not found and i < len(P):
            if isPrime(P[i]):
                res = P[i]
                found = True
            i += 1
        n -= 1
    return res

start_time = time.time()
print("Ans = {}".format(pe41()))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))
