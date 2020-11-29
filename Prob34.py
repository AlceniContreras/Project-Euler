#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Digit factorials
# ----------------

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

import math
suma = 0
for x in range(3, 1000000):
    s = list(map(int, str(x)))
    sum_fact = sum([math.factorial(i) for i in s])
    if x == sum_fact:
        suma += x
print(suma)