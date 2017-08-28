# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 23:33:55 2017

@author: wasabi
"""
import time
from algorithm import nCr


def pe595(N):
    T = {(1, 1): 1, (2, 1): 1, (2, 2): 1}
    S = {1: 0.0, 2: 1.0}
    F = {1: 1, 2: 2, 3: 6}

    def f(n):
        if n not in F:
            F[n] = f(n-1) * n
        return F[n]
    
    
    def t(n, k):
        if (n, k) not in T:
            if k < n:
                T[(n, k)] = nCr(n-1, k-1) * t(k, k)
            else:
                T[(n, k)] = f(n) - sum([t(n, i) for i in range(1, n)])
        return T[(n, k)]
    
    
    def s(n):
        if n not in S:
            S[n] = 0
            for k in range(2, n):
                S[n] += (s(k) + 1) * (t(n, k) / f(n))
            p = t(n, n) / f(n)
            S[n] = (S[n] + p) / (1 - p)
        return S[n]
    
    return round(s(N), 8)
    

start_time = time.time()
print("Answer: {}".format(pe595(52)))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
