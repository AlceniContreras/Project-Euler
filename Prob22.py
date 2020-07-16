# -*- coding: utf-8 -*-
# Names scores
# ------------

def value(n):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    m = list(n)
    for i in range(len(m)):
        m[i] = alphabet.index(m[i]) + 1
    return sum(m)

# Opening and cleaning the list of names
file = open('names.txt', 'r')
temp = file.read()
temp = temp.replace('"', '')

# Ordering the list of names
names = temp.split(',')
names.sort()

#Evaluating the score of every name and closing the file
scores = [(value(names[i]) * (i+1)) for i in range(len(names))]
file.close()

print(sum(scores))
