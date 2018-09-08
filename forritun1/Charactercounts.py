import string
count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))

strengur = input("Sladu inn einhverja setningu: ")

print ("Storir stafir: " , sum(1 for l in strengur if l.isupper()))
print ("Litlir stafir: " , sum(1 for l in strengur if l.islower()))
print ("Tolustafir: " , sum(1 for t in strengur if t.isdigit()))
print ("Punktar/Kommur :" , count(strengur, string.punctuation))