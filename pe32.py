# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 13:04:06 2017

@author: tring
"""
import time
from itertools import permutations


def pe32():
    N = [''.join(p) for p in permutations('123456789')]
    res = 0
    found = []
    
    for i in range(1, 3):
        for n in N:
            a = int(n[:i])
            b = int(n[i:5])
            c = int(n[5:])
            if a * b == c and c not in found:
                res += c
                found.append(c)
    return res

start_time = time.time()
print("Ans = {}".format(pe32()))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))
