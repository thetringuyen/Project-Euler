# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 14:03:02 2017

@author: tring
"""

import time
from math import factorial


def pe20(N):
    return sum([int(s) for s in str(factorial(N))])


start_time = time.time()
print("Answer: {}".format(pe20(100)))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
