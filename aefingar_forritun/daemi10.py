number = int(input("Sláðu inn tölu: "))
if 0 < number < 10:
    print("less than 10")
elif 20 >= number >= 10:
    print("between 10 and 20")
elif number <= 20:
    print("The value too high!")
elif number < 0:
    print("too low")