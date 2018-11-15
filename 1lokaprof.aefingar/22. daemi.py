low = int(input("sláðu inn tölu: "))
high = int(input("sláðu inn hærri tölu: "))
summa = 0
for number in range(low, high+1):
    summa += number
print(summa)