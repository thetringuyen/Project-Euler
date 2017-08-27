# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:45:26 2017

@author: tring
"""

import time
from algorithm import gcd

def pe5():
    res = 2
    for n in range(4, 21):
        g = gcd(res, n)
        res *= n // g
    return res


start_time = time.time()
print("Answer: {}".format(pe5()))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
