# -*- coding: utf-8 -*-
# Longest Collatz sequence
# ------------------------

x = 1000000

def collatz(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        count += 1
    return count

longest = 0

for i in range(2, x):
    newLongest = collatz(i)
    if newLongest > longest:
        r, longest = i, newLongest

print(r, longest)