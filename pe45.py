# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 21:28:45 2017

@author: tring
"""
import time


def pe45():
    n_p = 165
    found = False
    while not found:
        n_p += 1
        P = n_p * (3 * n_p - 1)
        n_t = int(P ** .5)
        found = (n_t & 1) and (n_t * (n_t + 1) == P)
    return int(n_t * (n_t + 1) / 2)

start_time = time.time()
print("Ans = {}".format(int(pe45())))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))
