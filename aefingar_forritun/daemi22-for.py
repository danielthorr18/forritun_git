low = int(input("Sláðu inn tölu: "))
high = int(input("Sláðu inn hærri tölu: "))
sum_of_all = 0
for item in range(low, high + 1):
    sum_of_all += item
print(sum_of_all)