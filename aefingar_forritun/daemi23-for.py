low = int(input("Sláðu inn tölu: "))
high = int(input("Sláðu inn hærri tölu: "))
sum_of_odd = 0

for item in range(low, high + 1):
    if item % 2 != 0:
        sum_of_odd += item
        
print(sum_of_odd)