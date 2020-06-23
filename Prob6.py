# -*- coding: utf-8 -*-
# Sum square difference 
# ---------------------

import numpy as np

n = 100

numbers = np.arange(1, n+1)
squareSum = sum(numbers)**2
sumSquares = sum(numbers**2)

print(squareSum - sumSquares)
