low = int(input("Sláðu inn tölu: "))
high = int(input("Sláðu inn hærri tölu: "))

for item in range(low, high + 1):
    if low < high:
        print(item)
    elif low >= high:
        print("low not lower than high")