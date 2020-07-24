#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Number spiral diagonals
# -----------------------

n = int(input("Size of the square matrix (must be an odd number): "))
top = (n + 1) // 2
elem = []
for i in range(1, top):
    a = (2 * i - 1) ** 2
    b = (2 * i + 1) ** 2
    c = 2 * i
    elem += list(range(a, b, c))
elem.append(n**2)

print(sum(elem))