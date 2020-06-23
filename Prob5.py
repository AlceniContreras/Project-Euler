# -*- coding: utf-8 -*-
# Smallest Multiple
# -----------------

import math

n = 20

def isPrime(x):
    for i in range(2, math.floor(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
        else:
            pass
    return True

def mcm(a, b, primes):
    result = 1
    for prime in primes:
        while a % prime == 0 or b % prime == 0:
            if a % prime == 0: 
                a = a / prime
            if b % prime == 0: 
                b = b / prime
            result *= prime
    return result

prod = 1
Primes = []
z = []

for x in range(1,n+1):
    z.append(x)
    if isPrime(x):
        Primes.append(x)

while len(z) >= 2:
    u = z[-1]
    v = z[-2]
    w = mcm(u, v, Primes[1::])
    z.pop()
    z.pop()
    z.append(w)

print(w)