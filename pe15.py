# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:58:28 2017

@author: tring
"""
import time
from algorithm import nCr


def pe15(N):
    return nCr(N * 2, N)


start_time = time.time()
print("Answer: {}".format(pe15(20)))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
