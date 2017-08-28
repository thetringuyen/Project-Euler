# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 15:02:32 2017

@author: tring
"""
import time


def pe31(N, A):
    global known
    
    if N == 0:
        return 1
    A = [a for a in A if a <= N]
    B = tuple(A)
    if len(A) < 1:
        return 0
    if (N, B) not in known:
        known[(N, B)] = pe31(N-A[-1], A) + pe31(N, A[:-1])
    return known[(N, B)]

start_time = time.time()
known = {}
A = [1, 2, 5, 10, 20, 50, 100, 200]
print("Ans = {}".format(int(pe31(200, A))))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))
