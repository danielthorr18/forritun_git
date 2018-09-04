my_int = int(input("Enter a positive integer: "))

while my_int > 0:
    if my_int % 2 == 1:
        my_int = my_int // 2
    else:
        my_int = my_int - 1
print(my_int)            
