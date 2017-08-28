# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 00:46:04 2017

@author: tring
"""
import time
from algorithm import bcdToDec, isPrime


def truncateBCD(n, left=0):
    if left:
        m = n
        count = 0
        o = 0
        while m > 0:
            m >>= 4
            count += 1
            o = (o << 4) + 15
        o >>= 4
        return o & n
    return n >> 4



def isTruncatablePrime(n):
    if not isPrime(bcdToDec(n)):
        return False
    
    for i in range(2):
        m = truncateBCD(n, i)
        while m > 0:
            if not isPrime(bcdToDec(m)):
                return False
            m = truncateBCD(m, i)
    return True


def pe37(nums=[2, 3, 5, 7], digits=[1, 3, 7, 9], found=0):
    new_nums = [d + (n << 4) for d in digits for n in nums]
    i, s = 0, 0
    while found < 11 and i < len(new_nums):
        if isTruncatablePrime(new_nums[i]):
            found += 1
            s += bcdToDec(new_nums[i])
        i += 1
    if found < 11:
        s += pe37(new_nums, digits, found)
    return s


start_time = time.time()
print("Ans = {}".format(int(pe37())))
print("Run time = {:0.0f}ms".format((time.time() - start_time) * 1000))
