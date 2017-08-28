# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 00:46:04 2017

@author: tring
"""
import time
from algorithm import bcdToDec, isPrime


def rotateBCD(n):
    m = n >> 4
    res = n & 0xF
    while m > 0:
        res <<= 4
        m >>= 4
    res |= (n >> 4)
    return res


def isCircularPrime(n):
    m = bcdToDec(n)
    if not isPrime(m):
        return False
    for i in range(len(str(m))-1):
        n = rotateBCD(n)
        if not isPrime(bcdToDec(n)):
            return False
    return True


def pe35():
    count = 4
    digits = [1, 3, 7, 9]
    nums = digits.copy()
    for i in range(2, 7):
        nums = [d + (n << 4) for d in digits for n in nums]
        for n in nums:
            if isCircularPrime(n):
                count += 1
    return count


start_time = time.time()
print("Ans = {}".format(int(pe35())))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))
