turns = int(input("Sláðu inn tölu: "))

sum_of_negative = 0
sum_of_positive = 0
how_many_pos = 0
how_many_neg = 0

for item in range(turns):
    pick = int(input("Sláðu inn tölu: "))
    if pick >= 0:
        how_many_pos += 1
        sum_of_positive += pick
    else:
        how_many_neg += 1
        sum_of_negative += pick

print("Sum of positive numbers", sum_of_positive)
print("how many positive numbers", how_many_pos)
print("Sum of negative numbers", sum_of_negative)
print("How many negative numbers", how_many_neg)
