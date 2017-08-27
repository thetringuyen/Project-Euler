# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:58:28 2017

@author: tring
"""

import time

def pe9(N):
    for a in range(3, (N-3)//3+1):
        for b in range(a+1, (N-a)//2+1):
            c = N - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c


start_time = time.time()
print("Answer: {}".format(pe9(1000)))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
