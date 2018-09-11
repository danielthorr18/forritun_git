a = int(input("Sláðu inn tölu: "))
b = int(input("Sláðu inn aðra tölu: "))

choice = int(input("Sláðu inn tölu: "))

if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)
elif choice ==3:
    print(a * b)
else:
    print("Invalid input")
