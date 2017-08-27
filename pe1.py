# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 18:17:18 2017

@author: tring
"""
import time

def pe1(N):
    return sum([n for n in range(1, N) if not (n % 3 and n % 5)])


start_time = time.time()
print("Answer: {}".format(pe1(1000)))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
