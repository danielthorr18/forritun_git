position = int(input("Input a position between 1 and 10: "))
new_pos = position

def move_right(new_pos):
    if new_pos == 10:
        return new_pos
    elif new_pos >= 1 and new_pos <= 10:
        return new_pos+1

def move_left(new_pos):
    if new_pos == 1:
        return new_pos
    elif new_pos <= 10 and new_pos >= 1:
        return new_pos-1


while True:
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    choice = input("Input your choice: ")
    
    if choice not in 'lr':
        print("New position is:", new_pos)
        break
    elif choice == "l":
        new_pos = move_left(new_pos)
    
    elif choice == "r":
        new_pos = move_right(new_pos)
    
    print("New position is:", new_pos)