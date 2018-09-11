turns = int(input("Sláðu inn tölu: "))

number_of_negativ = 0

for item in range(turns):

    pick = int(input("Sláðu inn tölu: "))
    if pick <= 0:
        number_of_negativ += 1
print(number_of_negativ)
