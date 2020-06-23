# -*- coding: utf-8 -*-
# 10001st prime number
# --------------------

import math

n = 10001

def isPrime(x):
    for i in range(2, math.floor(math.sqrt(x))+1):
        if x % i == 0:
            return False
        else:
            pass
    return True

primes = []
i = 2

while len(primes) < n:
    if isPrime(i):
        primes.append(i)
    i += 1

print(primes[-1])