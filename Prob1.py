# -*- coding: utf-8 -*-
# Multiples of 3 and 5
# --------------------

n = int(input("Ingrese un número entero: "))

multiples = []
i = 1

while i < n:
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)
    i += 1

print(sum(multiples))