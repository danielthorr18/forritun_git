age = int(input("Input age: ")) # Do not change this line
price = 30.0

if age >= 65:
	print(price*0.5)
elif age <= 5 and age > 0:
	print(price*0.0)
else:
	print(price)
