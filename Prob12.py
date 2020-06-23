# -*- coding: utf-8 -*-
# Highly divisible triangular number
# ----------------------------------

import math

n = 500

def numDivisors(x):
    divisors = [1]
    for i in range(2, math.floor(math.sqrt(x) + 1)):
        if x % i == 0:
            divisors.append(i)
    
    temp = []
    
    for j in divisors:
        temp.append(x//j)
    
    divisors += temp
    divisors = list(set(divisors))
    return(len(divisors))

triangular = [1]; i = 2

while numDivisors(triangular[-1]) < n:
    triangular.append(triangular[-1] + i)
    i += 1

print(triangular[-1])