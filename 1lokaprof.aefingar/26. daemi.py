turns = int(input("Sláðu inn innsláttarfjölda: "))
negativ = 0
for number in range(turns):
    pick = int(input("veldu þér tölu drengur!: "))
    if pick < 0:
        negativ += 1

print(negativ)
