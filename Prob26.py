#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Reciprocal cycles
# -----------------

# Listing all primes

from Euler import is_prime

primes = [i for i in range(2, 1000) if is_prime(i)]

# Calculating number of recursive digits

def cycle_digits(q):
    d = 1
    while pow(10, d) % q != 1:
        if pow(10, d) % q == 0:
            break
        d += 1
    return d

length_digits = [cycle_digits(x) for x in primes]

# Printing the result

longest = max(length_digits)
print(primes[length_digits.index(longest)])