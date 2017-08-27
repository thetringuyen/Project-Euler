# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:58:28 2017

@author: tring
"""
import time


def pe16(N):
    return sum([int(s) for s in str(N)])


start_time = time.time()
print("Answer: {}".format(pe16(2**1000)))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
