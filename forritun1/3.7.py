hole = 1

while hole <= 18:
    
    par = int(input("Par of hole{}: " .format(hole)))
    
    score = int(input("Score on hole {}: ".format(hole)))
    
    if par < score:
        myScore = score - par

        if myScore > 3:
            print("bad hole")
        elif myScore == 3:
            print("")