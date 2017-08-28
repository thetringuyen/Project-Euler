# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 13:23:02 2017

@author: tring
"""
import time
from math import factorial


def pe24(n, A=[a for a in range(10)]):
    if n == 0:
        A.sort(reverse=True)
        return ''.join([str(a) for a in A])
    m = factorial(len(A)-1)
    r = n % m
    i = n // m - (0 if r > 0 else 1)
    return str(A[i]) + pe24(r, [a for a in A if a != A[i]])
        

start_time = time.time()
print("Ans = {}".format(int(pe24(1000000))))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))