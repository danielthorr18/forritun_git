turns = int(input("Sláðu inn tölu: "))
sum_of_negative = 0
sum_of_positive = 0
for item in range(turns):
    pick = int(input("Sláðu inn tölu: "))
    if pick <=0:
        sum_of_negative += 1
    elif pick > 0:
        sum_of_positive += 1
print(sum_of_negative)
print(sum_of_positive)