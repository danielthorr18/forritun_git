LOWER_LIMIT = 1
UPPER_LIMIT = 10




def newPositionPrint(position):
    print("New position is: {}".format(position))

def movementChoice():
    movementChoice = input("l - for moving left \nr - for moving right \nAny other letter for quitting \nInput your choice: ")
    return movementChoice

def GameOverCheck(movement):
    if movement == 'l' or movement == 'r':
        return False
    else:
        return True


def positionChanger(movement, position):
    if movement == "l" and position > LOWER_LIMIT:
        position -= 1
    elif movement == "r" and position < UPPER_LIMIT:
        position += 1
    return position



def main():
    GameOver = False
    position = int(input("Input a position between 1 and 10: "))
    while GameOver == False:
        movement = movementChoice()
        GameOver = GameOverCheck(movement)
        position = positionChanger(movement, position)
        newPositionPrint(position)



main()

