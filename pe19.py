# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 16:11:32 2017

@author: wasabi
"""
import time
import datetime


def pe19():
    res = 0
    for i in range(1901, 2001):
        for j in range(1, 13):
            res += 1 if datetime.datetime(i, j, 1).weekday() == 6 else 0
    return res


start_time = time.time()
print("Answer: {}".format(pe19()))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
