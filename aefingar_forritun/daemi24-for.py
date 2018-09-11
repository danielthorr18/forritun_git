low = int(input("Sláðu inn tölu: "))
high = int(input("Sláðu inn hærri tölu: "))
sum_of_numbers = 0

for item in range(low, high + 1):
    if item % 3 == 0:
        sum_of_numbers += item
print(sum_of_numbers)