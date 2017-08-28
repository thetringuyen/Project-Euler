# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 01:46:44 2017

@author: tring
"""
import time


def isPalindromicBase2(n):
    b = bin(n)[2:]
    return b == b[::-1]


def pe36():
    N = [int(str(i) + str(i)[::-1]) for i in range(1000)]
    N += [int(str(i) + str(i)[:-1][::-1]) for i in range(1000)]
    return sum([n for n in N if isPalindromicBase2(n)])


start_time = time.time()
print("Ans = {}".format(int(pe36())))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))
