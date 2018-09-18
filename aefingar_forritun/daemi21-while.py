turns = int(input("Sláðu inn tölu: "))

counter = 0

while counter < turns:
    pick = int(input("Sláðu inn tölu: "))
    if pick % 2 == 1:
        print("þú valdir", pick)
    counter += 1