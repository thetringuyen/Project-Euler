# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 00:32:41 2017

@author: wasabi
"""
import time


def pe56(n):
    T = 0
    for a in range(1, n):
        for b in range(1, n):
            t = sum([int(s) for s in str(a ** b)])
            T = max(t, T)
    return T


start_time = time.time()
print("Ans = {}".format(pe56(100)))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))
