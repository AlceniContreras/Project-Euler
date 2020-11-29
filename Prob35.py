#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Circular primes
# ---------------

# The number, 197, is called a circular prime because all rotations of the digits: 
# 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

import numpy as np
import math
from Eulerlib.Euler import is_prime

def cyclic(N): 
    num = N
    exp = int(math.log10(N))
    perm = []
    while True: 
        num = (num % 10) * (10 ** exp) + (num // 10)
        perm.append(num)
        if (num == N): 
            break
    return perm

def circular(n, arr):
    terms = cyclic(n)
    for t in terms:
        if t not in arr:
            return False
    return True

target = 1000000
primes = [i for i in range(2, target) if is_prime(i)]
# print(is_prime(791))
# print(circular(179, primes))
primes2 = [i for i in primes if circular(i, primes)]
print(len(primes2))
