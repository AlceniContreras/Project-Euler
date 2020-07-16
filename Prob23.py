# -*- coding: utf-8 -*-
# Non-abundant sums
# -----------------

import numpy as np

def is_abundant(n):
    temp = np.arange(1, n)
    divisors = temp[n % temp == 0]
    return sum(divisors) > n

# Finding all the abundants numbers bellow 28123
top = 28123
a = np.arange(12, top)
b = np.array([is_abundant(i) for i in a])
abundants = a[b]

# Calculating the sum of abundant numbers, 2 in 2
s = len(abundants)
sum_abundants = []
for i in range(s):
    for j in range(i, s):
        sum_abundants.append(abundants[i] + abundants[j])

# Ordering and cleaning the sum
sum_abundants = list(set(sum_abundants))
sum_abundants.sort()

# Creating the list of non abundant sums
non_abundant_sum = []
for c in range(1, top):
    if c not in sum_abundants:
        non_abundant_sum.append(c)

print(abundants)
print(sum_abundants)
print(non_abundant_sum)
print(sum(non_abundant_sum))
