UpperCase = 0
LowerCase = 0
Digits = 0
Punctuation = 0
all_Punctuation = [',','.',':',';','"',"'",'-']

import string
string = input("Input word of your choice: ")

for i in string:
    if i.isupper():
        UpperCase += 1
    elif i.islower():
        LowerCase += 1
    elif i.isdigit():
        Digits += 1
    elif i in all_Punctuation:
        Punctuation += 1







print('{:>15s}{:>5d}'.format('Upper case', UpperCase))
print('{:>15s}{:>5d}'.format('Lower case', LowerCase))
print('{:>15s}{:>5d}'.format('Digits', Digits))
print('{:>15s}{:>5d}'.format('Punctuation', Punctuation))