#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Distinct powers
# ---------------

# Creating the full list of powers
n = 100
a = list(range(2, n + 1))
b = list(range(2, n + 1))
powers = [[i ** j for i in a] for j in b]

# Eliminating the duplicates
powers_unique = []
for row in powers:
    for elem in row:
        if elem not in powers_unique:
            powers_unique.append(elem)

print(len(powers_unique))
