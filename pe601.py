# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 01:50:03 2017

@author: tring
"""
import time
from algorithm import gcd


def pe601():
    A = {1: [2, 2], 2: [3, 2]}
    
    def a(s):
        if s not in A:
            A[s] = a(s-1).copy()
            while A[s][0] % s != 1:
                A[s][0] += A[s][1]
            g = gcd(A[s][1], s)
            A[s][1] *= s // g
        return A[s]
    
    
    def P(s, N):
        [n, m] = a(s)
        res = 0
        while n < N:
            if n % (s + 1) != 1:
                res += 1
            n += m
        return res
    
    res = 0
    for i in range(1, 32):
        res += P(i, 4 ** i)
    return res

start_time = time.time()
print("Answer: {}".format(pe601()))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
