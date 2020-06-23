# -*- coding: utf-8 -*-
# Largest prime factor
# --------------------

import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
        else:
            pass
    return True

n = 600851475143

factors = []
primes = []
temp = []

for i in range(2,int(math.sqrt(n))+1):
    if n % i == 0:
        factors.append(i)

for j in range(len(factors)):
    temp.append(int(n/factors[j]))

factors += temp
factors = list(set(factors))
factors.sort()

for k in range(len(factors)):
    if isPrime(factors[k]):
        primes.append(factors[k])

print(factors)
print(primes)