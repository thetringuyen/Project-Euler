# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:23:51 2017

@author: tring
"""
import time


def pe49():
    res = 1
    n = 1000
    while n <= 3340:
        if n != 1487 and isPrime(n):
            m = n + 3330
            if isPrime(m) and sorted(str(n)) == sorted(str(m)):
                k = m + 3330
                if isPrime(k) and sorted(str(k)) == sorted(str(m)):
                    return(str(n) + str(m) + str(k))
        n += 1

start_time = time.time()
print("Ans = {}".format(int(pe49())))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))
