# -*- coding: utf-8 -*-
# Even Fibbonacci numbers
# -----------------------

fibb = [1, 2]
suma = 0

while fibb[-1] < 4000000:
    fibb.append(fibb[-1] + fibb[-2])

fibb.pop()

for i in range(len(fibb)):
    if fibb[i] % 2 == 0:
        suma += fibb[i]

print(suma)