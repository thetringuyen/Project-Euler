# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:31:34 2017

@author: tring
"""

import time

def pe4():
    res = 0
    n = 990
    while n >= 100:
        m = 999
        while m >= 100:
            l = m * n
            s = str(l)
            if s == s[::-1]:
                res = max(res, l)
            m -= 1
        n -= 11
    return res


start_time = time.time()
print("Answer: {}".format(pe4()))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
