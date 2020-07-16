# -*- coding: utf-8 -*-
# Amicable numbers
# ----------------

import numpy as np

def divisors(x):
    temp = np.arange(1, x)
    divisors = x % temp == 0
    return(temp[divisors])

n = 10000

list_divisors = {i: sum(divisors(i)) for i in range(2, n)}
new_list_divisors = list_divisors.copy()

for i, j in list_divisors.items():
    if j == 1 or i == j or j >= n:
        del new_list_divisors[i]

amicables = {}

for k in new_list_divisors.keys():
    try:
        v = new_list_divisors[k]
        if k == new_list_divisors[v]:
            amicables[k] = v
    except KeyError:
        pass

print(amicables)
print(sum(amicables.keys()))