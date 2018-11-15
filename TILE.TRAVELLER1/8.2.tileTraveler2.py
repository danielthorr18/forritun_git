x = 1
y = 1
valid_direction =str("n")
victory = False
print("You can travel: (N)orth.")



def move_player(valid_direction,x,y):
    direction = input("Direction: ")
    direction = direction.lower()
    if not direction in valid_direction:
        print("Not a valid direction!")
    else:
        
        #if not victory:
           # print("You can travel: ", end = "")
        if direction == "n":
            y += 1
        elif direction == "s":
            y -= 1
        elif direction == "e":
            x += 1
        elif direction == "w":
            x -= 1
        if x == 1 and y == 1:
            valid_direction = "n"
            print("(N)orth.")
        elif x == 1 and y == 2:
            valid_direction = "nes"
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif x == 1 and y == 3:
            valid_direction = "es"
            print("You can travel: (E)ast or (S)outh.")
        elif x == 2 and y == 1:
            valid_direction = "n"
            print("You can travel: (N)orth.")
        elif x == 2 and y == 2:
            valid_direction = "sw"
            print("You can travel: (S)outh or (W)est.")
        elif x == 2 and y == 3:
            valid_direction = "ew"
            print("You can travel: (E)ast or (W)est.")
        elif x == 3 and y == 2:
            valid_direction = "ns"
            print("You can travel: (N)orth or (S)outh.")  
        elif x == 3 and y == 3:
            valid_direction = "sw"
            print("You can travel: (S)outh or (W)est.")
    return valid_direction,x,y

def check_if_victory(x,y,victory):
    if x == 3 and y == 1:
        victory = True
        print("Victory!")
        return victory
    

while not victory: 
    victory=check_if_victory(x,y,victory)
    if victory:
        break
    valid_direction,x,y=move_player(valid_direction,x,y)