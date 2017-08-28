# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 02:48:10 2017

@author: tring
"""
import time


def pe48():
    c = 10**10
    res = 0
    for i in range(1, 1001):
        res = (res + i**i) % c
    return res
    

start_time = time.time()
print("Ans = {}".format(int(pe48())))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))
