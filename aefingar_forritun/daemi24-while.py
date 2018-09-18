low = int(input("Sláðu inn tölu: "))
high = int(input("Sláðu inn hærri tölu: "))

sum_of_tings = 0

while low <= high:
    if low % 3 ==0:
        sum_of_tings += low
    low += 1
print(sum_of_tings)
