low = int(input("Sláðu inn tölu: "))
high = int(input("Sláðu inn hærri tölu: "))

sum_of_odd = 0

while low <= high:
    if low % 2 == 1:
        sum_of_odd += low
    low += 1
print(sum_of_odd)
