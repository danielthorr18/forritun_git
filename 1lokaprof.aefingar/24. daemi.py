low = int(input("sláðu inn tölu: "))
high = int(input("sláðu inn hærri tölu: "))
summan_min = 0
for number in range(low, high+1):
    if number % 3 ==0:
        summan_min += number
print(summan_min)
