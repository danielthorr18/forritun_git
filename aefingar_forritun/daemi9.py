num1 = int(input("Sláðu inn tölu: "))
num2 = int(input("Sláðu inn aðra tölu: "))
num3 = int(input("Sláðu inn þriðju töluna: "))

if num2 > num1 < num3:
    print(num1)
elif num1 > num2 < num3:
    print(num1)
else:
    print(num3)