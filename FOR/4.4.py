m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

if m > n:
    m, n = n, m
    
for number in range(m, 0, -1):
    if m % number ==0 and n % number ==0:
        print(number)
        break