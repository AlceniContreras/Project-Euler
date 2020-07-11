# -*- coding: utf-8 -*-
# Counting Sundays
# ----------------

import numpy as np

years = list(range(1901, 2001))
is_bisiesto = [y % 4 == 0 for y in years]

days = {0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'}

increment = np.array(is_bisiesto)+1

first_jan = np.array([2])           # first day of every year
for i in range(len(years)-1):
    temp = first_jan[i] + increment[i]
    first_jan = np.append(first_jan, [temp])
first_jan = first_jan % 7

regular = np.array([0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334])      # first day of every month in regular years, starting on sunday
regular = regular % 7
leap = np.array([0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335])         # first day of every month in leap years, starting on sunday
leap = leap % 7


first_days = np.array([(leap if i == True else regular) for i in is_bisiesto])   # first day of every month during the 20th century
for j in range(len(years)):
    first_days[j] = first_days[j] + first_jan[j]
first_days = first_days % 7

# Print of Results:
for x in range(7):
    print('There are', np.sum(first_days == x), days[x] + 's')