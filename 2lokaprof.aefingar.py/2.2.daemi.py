listinn = []

size = int(input("sláðu inn stærð lista: "))

for number in range(size):
    pick = int(input("sláðu númer gamli: "))
    listinn.append(pick)

target = int(input("sláðu inn tölu, til að athuga hvort hún sé í listanum: "))
targetInList = False

for number in listinn:
    if number == target:
        targetInList = True
        break

if targetInList == True:
    print("{}, sem þú valdir, er í listanum".format(target))
        
else:
    print("{} er ekki í listanum gamli, drullastu í burtu!".format(target))   

        
