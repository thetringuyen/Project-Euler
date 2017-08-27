# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:58:28 2017

@author: tring
"""

import time
from algorithm import nextPrime

def pe7(N):
    count = 1
    res = 0
    for n in nextPrime():
        if count == N:
            res = n
            break
        count += 1
    return res


start_time = time.time()
print("Answer: {}".format(pe7(10001)))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
