weight_str = input("Weight (kg): ") # do not change this line
height_str = input("Height (cm): ") # do not change this line

weight_float = float(weight_str)
height_float = float(height_str)

height_float = height_float / 100

bmi = weight_float / (height_float**2)

print("BMI is: ", bmi) # do not change this line
