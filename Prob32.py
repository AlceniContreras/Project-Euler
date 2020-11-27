#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Pandigital products
# -------------------

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 
# to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, 
# multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be 
# written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include 
# it once in your sum.

products = {} 

for i in range(1000):
    for j in range(10000):
        k = i * j
        x = str(i) + str(j) + str(k)
        if len(x) == 9:
            nr = set(x)
            if set(map(int, nr)) == set(range(1, 10)):
                products[k] = [i, j]

print(products)
print(sum(products.keys()))
