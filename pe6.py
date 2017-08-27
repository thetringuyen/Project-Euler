# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:45:26 2017

@author: tring
"""

import time

def pe6(N):
    return int((N*(N+1)/2)**2 - sum([n**2 for n in range(N+1)]))

start_time = time.time()
print("Answer: {}".format(pe6(100)))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
