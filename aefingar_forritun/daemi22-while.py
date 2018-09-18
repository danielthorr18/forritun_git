low = int(input("Sláðu inn tölu: "))
high = int(input("Sláðu inn hærri tölu: "))

sum_of_all = 0

while low <= high:
    sum_of_all += low
    low += 1
print(sum_of_all)
