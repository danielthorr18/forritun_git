n = int(input("Input a natural number: ")) # Do not change this line
prime = True
count = 2
while count < n:
    if n % count == 0:
        prime = False
    count += 1        
    
if prime:
    print("Prime")
else:
    print("!Prime")