# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 18:32:09 2017

@author: tring
"""
import time
from algorithm import nextPrime

def pe3(N):
    res = 0
    for p in nextPrime():
        if p > N:
            break
        if not N % p:
            res = p
            N //= p
    return res


start_time = time.time()
print("Answer: {}".format(pe3(600851475143)))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
