# -*- coding: utf-8 -*-
# Special Pythagorean triplet
# ---------------------------

n = 1000

a = 1; b = 1; c = 1
while a + b + c != n+1:
    for i in range(a, n):
        b = i
        c = (a**2 + b**2)**0.5
        d = a + b + c
        if d == n:
            break
    a += 1
a = a - 1; c = int(c)
print(a,b,c)
print(a*b*c)