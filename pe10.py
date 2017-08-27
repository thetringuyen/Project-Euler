# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:58:28 2017

@author: tring
"""

import time
from algorithm import primeSeive

def pe10(N):
    res = 0
    seive = primeSeive(N)
    stop = False
    while not stop:
        try:
            n = next(seive)
        except StopIteration:
            stop = True
        if not stop:
            res += n
            #print(n)
    return res

start_time = time.time()
print("Answer: {}".format(pe10(2000000)))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
