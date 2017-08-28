# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 17:07:26 2017

@author: wasabi
"""

import time
from algorithm import gcd, primeSeive


def pe598(n):
    def countFactor(n, p):
        c = 0
        m = n
        while m >= p:
            m //= p
            c += m
        return c
    
    
    def isPossible(a, b, i):
        for j in range(D[i]+1, 1, -1):
            while not (a % j):
                a //= j
            while not (b % j):
                b //= j
        return a == 1 and b == 1


    def dfs(a, b, i):
        if i >= len(P):
            return a == b
        g = gcd(a, b)
        a, b = a//g, b//g
        if (a, b, i) not in known:
            if isPossible(a, b, i):
                c = 0
                for j in range(D[i]+1):
                    c += dfs(a*(j+1), b*(D[i]-j+1), i+1)
                known[(a, b, i)] = c
            else:
                known[(a, b, i)] = 0
        return known[(a, b, i)]

    P = [p for p in primeSeive(n)]
    D = [countFactor(n, p) for p in P]
    known = {}
    return dfs(1, 1, 0) // 2

start_time = time.time()
print("Answer: {}".format(pe598(100)))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
