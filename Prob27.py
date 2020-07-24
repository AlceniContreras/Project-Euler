#!/usr/bin/python3
# -*- coding: utf-8-*-
# Quadratic primes
# ----------------

from Euler import is_prime, get_key

def count_primes(a, b):
    def f(n):
        return n ** 2 + a * n + b
    count = 0
    while is_prime(f(count)):
        count += 1
    return count

# Generating the loop lists
a = list(range(-1000, 1000))
b = [i for i in range(2, 1000) if is_prime(i)]

# Calculating the number of primes each pair (a, b) generates
full_list = {}
for i in a:
    for j in b:
        full_list[(i, j)] = count_primes(i, j)

# Presenting results
target = max(full_list.values())
coef_1, coef_2 = get_key(full_list, target)
print(coef_1 * coef_2)