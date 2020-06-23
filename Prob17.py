#-*- coding: utf-8 -*-
# Number letter counts
# --------------------

stop = 1000

num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13:'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}

def under_100(n):
    try:
        return num2words[n]
    except KeyError:
        try: 
            tens, units = divmod(n, 10)
            return num2words[tens*10] + num2words[units].lower()
        except KeyError:
            return 'Out of range'

def spell_numbers(x):
    if x == 1000:
        spelled = 'One thousand'        
    elif 100 <= x < 1000:
        hundreds, remainder = divmod(x, 100)
        spelled = num2words[hundreds] + ' hundred'
        if remainder != 0:
            spelled += ' and ' + under_100(remainder).lower()
    elif x < 100:
        spelled = under_100(x)
    else:
        spelled = 'Out of range'
    return spelled

spelled = [spell_numbers(i) for i in range(1, stop + 1)]
temp = ""
for num in spelled:
    temp += num
temp = temp.replace(" ", "")
print(len(temp))