top_num = int(input("Input a number between 0 and 999: "))

for i in range(0,top_num):
    if i < 1000 and i > 99:
        fyrsta = i // 100
        mid = i // 10 % 10
        seinni = i % 10
        summa = seinni ** 3 + mid ** 3 + fyrsta ** 3
        if summa == i:
            print(i)
    elif i < 100 and i > 9:
        fyrsta = i // 10
        seinni = i % 10
        summa = fyrsta ** 2 + seinni ** 2
        if summa == i:
            print(i)
    else:
        print(i)


    