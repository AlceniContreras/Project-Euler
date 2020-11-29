#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Digit cancelling fractions
# --------------------------

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting 
# to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by 
# cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value,
# and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value 
# of the denominator.

product = [1, 1]

for n in range(10, 100):
    for d in range(n + 1, 100):
        if (n % 10 == 0) | (d % 10 == 0):
            pass
        elif (n % 11 == 0) | (d % 11 == 0):
            pass
        else:
            N = {n // 10, n % 10}
            D = {d // 10, d % 10}
            if N == D:
                pass
            elif N & D:
                el_1 = (N - D).pop()
                el_2 = (D - N).pop()
                if n / d == el_1 / el_2:
                    product[0] *= el_1 
                    product[1] *= el_2

import math
mcm = math.gcd(product[0], product[1])
print(product[1] // mcm)