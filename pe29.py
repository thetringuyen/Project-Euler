# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 14:23:29 2017

@author: tring
"""
import time


def pe29(N):
    res = set(a**b for a in range(2, N+1) for b in range(2, N+1))
    return len(res)

start_time = time.time()
print("Ans = {}".format(int(pe29(100))))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))
