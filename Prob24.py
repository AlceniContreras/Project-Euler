# -*- coding: utf-8 -*-
# Lexicographic permutations
# --------------------------

# Listing all the permutations

from itertools import permutations

top = 9
li = [str(i) for i in range(top + 1)]
perm = list(permutations(li))

# Calling the 1000000th number of the list

n = 1000000
x = perm[n-1]
num = ''
for i in x:
    num += i

print(num)
