def the_range(number):
    if number in range(2, 554):
        return True
    else:
        return False

num = int(input("Enter a number: "))

if the_range(num) == True:
    print(num, "is inside the range")
else:
    print(num, "is outside the range!")

# You call the function here