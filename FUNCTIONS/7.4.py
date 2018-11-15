def isprime(tala):
    n = 2
    for n in range(2, tala):
        if (tala % n == 0):
            return False
    else:
            return True

        
    
num = int(input("Input an integer greater than 1: "))

if isprime(num):
    print(num, "is a prime")
else:
    print(num, "is not a prime")   