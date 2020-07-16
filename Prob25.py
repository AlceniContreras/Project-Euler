# -*- coding: utf-8 -*-
# 1000-digit Fibonacci number
# ---------------------------

import math

fib = [0, 1]
dig = 1000
i = 1

while math.log10(fib[-1]) < dig - 1:
    i += 1
    fib.append(fib[i-1] + fib[i-2])

print(i)
