# -*- coding: utf-8 -*-
# Summation of primes
# -------------------

import math

n = 2000000

def isPrime(x):
    for i in range(2, math.floor(math.sqrt(x))+1):
        if x % i == 0:
            return False
        else:
            pass
    return True

primes = [2]; i = 3

while primes[-1] < n:
    if isPrime(i):
        primes.append(i)
    i += 2
primes.pop()

print(sum(primes))