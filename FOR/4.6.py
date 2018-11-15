top_num = int(input("Upper number for the range: ")) # Do not change this line

for num in range(1, top_num+1):
    summa = 0
    for i in range(1, num):
        if (num % i) == 0:
            summa += i
    if num == summa:
        print(num)