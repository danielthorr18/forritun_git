turns = int(input("sláðu inn innsláttarfjölda: "))
positiv_count = 0
negativ_count = 0
for number in range(turns):
    pick = int(input("sláðu inn tölu: "))
    if pick < 0:
        negativ_count += 1
    elif pick > 0:
        positiv_count += 1

print(("þú slóst inn {} neikvæðar tölur og {} jákvæðar tölur").format(negativ_count, positiv_count))