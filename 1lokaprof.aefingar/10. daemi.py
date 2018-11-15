number = input("sladu inn numer: ")
n1 = int(number)

if n1 < 10:
    print("less than 10")
elif n1 >= 20:
    print("value is too high!")
elif n1 == 0:
    print("value is too low!")
else:
    print("Value is between 10 and 20")