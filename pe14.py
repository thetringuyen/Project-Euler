# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:58:28 2017

@author: tring
"""
import time


def pe14(N):
    C = {1: 1}
    res = 1
    res_c = 1
    for i in range(1, N):
        if i not in C:
            n = i
            c = 0
            while n >= i:
                c += 1
                if n & 1:
                    n += (n << 1) + 1
                else:
                    n >>= 1
            C[i] = c + C[n]
        if C[i] > res_c:
            res, res_c = i, C[i]
    return res


start_time = time.time()
print("Answer: {}".format(pe14(1000000)))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
