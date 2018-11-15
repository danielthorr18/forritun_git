turns = int(input("Sláðu inn innsláttarfjölda: "))
positiv_count = 0
positiv = 0
negativ_count = 0
negativ = 0
for number in range(turns):
    pick = int(input("sláðu inn tölu: "))
    if pick > 0:
        positiv_count +=1
        positiv += pick
    elif pick < 0:
        negativ_count +=1
        negativ += pick

print(("þú slóst inn {} neikvæðar tölur og {} jákvæðar tölur").format(negativ_count, positiv_count))
print(("summa neikvæðra talna er {} og summa jákvæðra talna er {}").format(negativ, positiv))




        

