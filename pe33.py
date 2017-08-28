# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 18:37:41 2017

@author: wasabi
"""
import time
from algorithm import gcd


def reduceFactor(a, b):
    g = gcd(a, b)
    return a//g, b//g


def pe33():
    m, n = 1, 1
    for i in range(1, 10):
        for j in range(1, 10):
            if i != j:
                for k in range(1, 10):
                    a = i * 10 + k
                    b = k * 10 + j
                    if a/b == i/j:
                        m *= a
                        n *= b
    m, n = reduceFactor(m, n)
    return n


start_time = time.time()
print("Ans = {}".format(pe33()))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))