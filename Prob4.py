# -*- coding: utf-8 -*-
# Largest palindrome product
# --------------------------

def isPalindrome(x):
    y = str(x)
    return y[::-1] == y

palindromes = []

for i in range(900,1000):
    for j in range(i,1000):
        z = i*j
        if isPalindrome(z):
            palindromes.append(i * j)

palindromes.sort()
print(palindromes[-1])