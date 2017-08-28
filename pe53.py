# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 18:16:16 2017

@author: wasabi
"""
import time
from algorithm import nCr


def pe53(N, M):
    c = 0
    for n in range(1, N + 1):
        for r in range(1, n // 2 + 1):
            mod = 1 + (2 * r != n)
            if nCr(n, r) > M:
                c += mod
    return c


start_time = time.time()
print("Ans = {}".format(pe53(100, 1000000)))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))

