# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 16:11:32 2017

@author: wasabi
"""
import time

def pe17():
    wordCounts ={0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4,
                 6: 3, 7: 5, 8: 5, 9: 4, 10: 3,
                 11: 6, 12: 6, 13: 8, 14: 8, 15: 7,
                 16: 7, 17: 9, 18: 8, 19: 8,
                 20: 6, 30: 6, 40: 5, 50: 5,
                 60: 5, 70: 7, 80: 6, 90: 6}

    def getNumWorldLen(N):
        n = [N // 1000, (N % 1000) // 100, N % 100]
        c = 0
        if n[0] > 0:
            c += wordCounts[n[0]] + 8
        if n[1] > 0:
            c += wordCounts[n[1]] + 7
            if n[0] > 0:
                c += 3
        if n[2] > 0:
            if n[1] > 0:
                c += 3
            if n[2] < 20:
                c += wordCounts[n[2]]
            else:
                c += wordCounts[n[2]//10*10] + wordCounts[n[2]%10]
        return c

    c = 0
    for i in range(1, 1001):
        c += getNumWorldLen(i)
    return c


start_time = time.time()
print("Answer: {}".format(pe17()))
print("Run time: {:0.2f}ms".format((time.time() - start_time) * 1000))
