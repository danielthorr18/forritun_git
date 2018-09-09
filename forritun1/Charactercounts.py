strengur = input("Enter a sentence: ")
kommur = [',','.',':',';','"',"'",'-']
storir = 0
litlir = 0
tala = 0
punktur = 0

for i in strengur:
    if i.islower():
        litlir = litlir + 1
    elif i.isupper():
        storir = storir + 1
    elif i.isdigit():
        tala = tala + 1
    elif i in kommur:
        punktur = punktur + 1

print('{:>15s}{:>5d}'.format('Upper case', storir))
print('{:>15s}{:>5d}'.format('Lower case', litlir))
print('{:>15s}{:>5d}'.format('Digits', tala))
print('{:>15s}{:>5d}'.format('Punctuation', punktur))
