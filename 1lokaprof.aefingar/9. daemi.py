number1 = input("sladu inn numer: ")
number2 = input("sladu inn annad numer: ")
number3 = input("sladu inn þridja numerid: ")

n1 = int(number1)
n2 = int(number2)
n3 = int(number3)

if n2 > n1 < n3:
    print(n1)
elif n1 > n2 < n3:
    print(n2)
else:
    print(n3)