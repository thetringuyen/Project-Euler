# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 17:40:13 2017

@author: tring
"""
import time
from math import factorial
from itertools import combinations_with_replacement as C


def pe34():
    f = [factorial(i) for i in range(10)]
    max_digit = 2
    while len(str(max_digit*f[9])) >= max_digit:
        max_digit += 1
    N = []
    res = 0
    for i in range(2, max_digit+1):
        N = [''.join(n) for n in C('1234567890', i)]
        for n in N:
            p = str(sum(f[int(s)] for s in n))
            if sorted(p) == sorted(n):
                res += int(p)
    return res
    

start_time = time.time()
print("Ans = {}".format(int(pe34())))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))
