# Til að fara í austur hækkar x-ás um 1, til þess að fara í vestur lækkaru x-ás um 1, 
# Til þess að fara í suður þá lækkary y-ás um 1, til þess að fara í norður þá hækkar y-ás um 1
# Búum til breytu sem heitir valid_direction sem segjir okkur hvaða átt er hægt að fara í að hverju sinni.
# Búum til bool breytu "victory" sem er False. 
# Við notum while loopu sem keyrir þar til breytan "victory" er orðin True (while not victory)
# Gera direction breytu þar sem notandi getur sett inn nýja átt í hverri ítrun, 
# ef áttin er ekki valid þá prentar kóðinn út "Not a valid direction" annars færist hann í þá átt sem slegin er inn 


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