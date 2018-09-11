turns = int(input("Sláðu inn tölu: "))

sum_of_negativ = 0

for item in range(turns):
    pick = int(input("Sláðu inn tölu: "))
    if pick <= 0:
        sum_of_negativ += pick
print(sum_of_negativ)

