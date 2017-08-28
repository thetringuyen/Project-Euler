# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 14:06:35 2017

@author: tring
"""
import time


def pe25(N):
    n, n1 = 1, 1
    res = 2
    while len(str(n1)) < N:
        n, n1 = n1, n + n1
        res += 1
    return res

start_time = time.time()
print("Ans = {}".format(int(pe25(1000))))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))