low = int(input("Sláðu inn tölu: "))
high = int(input("Sláðu inn hærri tölu: "))
sum_of_tings = 0

for item in range(low, high + 1):
    if item % 3 ==0 or item % 5 ==0:
        sum_of_tings += item
print(sum_of_tings)