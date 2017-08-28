# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:18:23 2017

@author: tring
"""
import time

def pe67():
    with open('pe67_input.txt') as f:
        lines = f.read().splitlines()
    A = [[int(s) for s in l.split(' ')] for l in lines]
    n = len(A) - 2
    for i in range (n, -1, -1):
        m = len(A[i])
        for j in range(m):
            A[i][j] += max(A[i+1][j], A[i+1][j+1])
    return A[0][0]


start_time = time.time()
print("Answer: {}".format(pe67()))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))

