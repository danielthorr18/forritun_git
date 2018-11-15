d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line
if d1 <= 0 or d1 > 6 or d2 <= 0 or d2 > 6:
	print("Invalid input")
else:
	outcome = d1 + d2
	if outcome == 7 or outcome == 11:
		print("Winner")
		
	elif outcome == 2 or outcome == 3 or outcome == 12:
		print("Loser")
	else:
		print(outcome)
