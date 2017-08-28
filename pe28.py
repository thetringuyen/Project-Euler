# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 14:15:18 2017

@author: tring
"""
import time


def pe28(N):
    res = 1
    for n in range(3, N+1, 2):
        res += 4 * ((n-2) ** 2) + 10 * (n-1)
    return res

start_time = time.time()
print("Ans = {}".format(int(pe28(1001))))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))
