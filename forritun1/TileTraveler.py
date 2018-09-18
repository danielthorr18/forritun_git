x = 1
y = 1
valid_direction = "n"
victory = False
print("You can travel: (N)orth.")

while not victory:
    direction = input("Direction: ")
    direction = direction.lower()   
    if not direction in valid_direction:
        print("Not a valid direction!")
    else:
        if direction == "n":
            y += 1
        elif direction == "s":
            y -= 1
        elif direction == "e":
            x += 1
        elif direction == "w":
            x -= 1

        if x == 3 and y == 1:
            victory = True
            print("Victory!")
            
        else : print("You can travel: ", end = "") 

        if x == 1 and y == 1:
            valid_direction = "n"
            print("(N)orth.")
        elif x == 1 and y == 2:
            valid_direction = "nes"
            print("(N)orth or (E)ast or (S)outh.")
        elif x == 1 and y == 3:
            valid_direction = "es"
            print("(E)ast or (S)outh.")
        elif x == 2 and y == 1:
            valid_direction = "n"
            print("(N)orth.")
        elif x == 2 and y == 2:
            valid_direction = "sw"
            print("(S)outh or (W)est.")
        elif x == 2 and y == 3:
            valid_direction = "ew"
            print("(E)ast or (W)est.")
        elif x == 3 and y == 2:
            valid_direction = "ns"
            print("(N)orth or (S)outh.")  
        elif x == 3 and y == 3:
            valid_direction = "sw"
            print("(S)outh or (W)est.")