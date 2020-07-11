# -*- coding: utf-8 -*-
# Factorial digit sum
# -------------------

import math
n = 100
fact = str(math.factorial(n))

x = sum(map(int, fact))
print(x)