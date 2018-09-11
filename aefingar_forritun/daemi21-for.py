turns = int(input("Input the number of turns: "))

for item in range(turns):
    pick = (input("Input number: "))
    if item % 2 !=0:
        print("you picked", pick)