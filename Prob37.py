#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Truncable primes
# ----------------

from Eulerlib import Euler

def truncableR(x, arr):
    while (x in arr) & (x > 0):
        x = x // 10
    return x == 0

def truncableL(x, arr):
    while (x in arr) & (x > 0):
        i = len(str(x))
        x = x % (10 ** (i-1))
        if i == 1:
            x = 0
    return x == 0

pr = Euler.get_primes(1000000)
trunc = []

for i in pr:
    if truncableR(i, pr) & truncableL(i, pr):
        trunc.append(i)
        if len(trunc) == 15:
            break

print(sum(trunc[4:]))
