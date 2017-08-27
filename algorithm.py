# -*- coding: utf-8 -*-

from functools import reduce


def isPrime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if not (n & 1):
        return False
    if n < 9:
        return True
    if not (n % 3):
        return False
    f = 5
    while f ** 2 <= n:
        if not (n % f) or not (n % (f+2)):
            return False
        f += 6
    return True


def nextPrime(n=2):
    while True:
        if isPrime(n):
            yield n
        n += 2 if n & 1 else 1       


def primeSeive(n):
    yield 2
    seive_bound = (n-1) // 2
    seive = [0 for i in range(seive_bound + 1)]
    cross_limit = (int(n ** 0.5) - 1) // 2
    for i in range(1, cross_limit + 1):
        if not seive[i]:
            for j in range(2*i*(i+1), seive_bound+1, 2*i+1):
                seive[j] = 1
    for i in range(1, seive_bound+1):
        if not seive[i]:
            yield 2*i+1
            
            
def countDivisors(n, P=None):
    res = 1
    if P is None:
        P = [p for p in primeSeive(n)]
    for p in P:
        if p*p > n:
            res *= 2
            break
        pwr = 1
        while not n % p:
            pwr += 1
            n //= p
        res *= pwr
        if n == 1:
            break
    return res



def nCr(n, r):
    if n < r:
        return 0
    r = min(r, n-r)
    if r == 0:
        return 1
    num = reduce((lambda x, y: x*y), range(n, n-r, -1))
    den = reduce((lambda x, y: x*y), range(1, r+1))
    return num//den


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if not a & 1:
        if not b & 1:
            return gcd(a >> 1, b >> 1) << 1
        else:
            return gcd(a >> 1, b)
    if not b & 1:
        return gcd(a, b >> 1)
    return gcd((max(a, b) - min(a, b)) >> 1, min(a, b))


def decToBCD(n):
    m = 0
    for s in str(n):
        m = (m << 4) + int(s)
    return m


def bcdToDec(n):
    if n <= 0:
        return 0
    m = ''
    while n > 0:
        m = str(n & 0xF) + m
        n >>= 4
    return int(m)
