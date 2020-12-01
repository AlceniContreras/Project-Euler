#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Double-base palindromes
# -----------------------

# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 
# and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def base2(N):
    binary = ''
    while N > 1:
        binary += str(N % 2)
        N = N // 2
    binary += str(N)
    return int(binary[::-1])

def isPalindromic(x):
    y = str(x)
    if y == y[::-1]:
        return True
    return False

target = 1000000
palindromics = [i for i in range(1, target) if (isPalindromic(i) & isPalindromic(base2(i)))]
print(sum(palindromics))
