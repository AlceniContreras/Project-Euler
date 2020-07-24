#!/usr/bin/python3
# -*-coding: utf-8 -*-
# Digit fifth powers
# ------------------

n = 5
lim = 10 ** (n + 1)
digit_fifth_powers = []

def digits(n):
    temp = str(n)
    return(list(map(int, temp)))

for x in range(2, lim):
    y = digits(x)
    summa = 0
    for i in y:
        summa += i ** n
    if x == summa:
        digit_fifth_powers.append(x)

print(digit_fifth_powers)
print(sum(digit_fifth_powers))
