# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 02:24:57 2017

@author: tring
"""
import time


def pe40():
    f = [9*(i+1)*10**i for i in range(6)]
    d = 1
    for i in range(7):
        n = 10**i
        j = 1
        while n >= f[j-1]:
            n -= f[j-1]
            j += 1
        r = n % j
        m = (n // j) + 10**(j-1) - (0 if r else 1)
        r = j if r == 0 else r
        d *= int(str(m)[r-1])
    return d


start_time = time.time()
print("Ans = {}".format(int(pe40())))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))
