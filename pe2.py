# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 18:21:42 2017

@author: tring
"""
import time


def pe2(N):
    fn, fn1 = 1, 2
    res = 2
    while fn1 <= N:
        fn, fn1 = fn1, fn + fn1
        res += 0 if fn1 & 1 else fn1
    return res


start_time = time.time()
print("Answer: {}".format(pe2(4000000)))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
