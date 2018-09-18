inital_value = int(input("Initial value: "))
step_int = int(input("Step: "))
Sum_of_series = 0
while Sum_of_series < 100:
    for step in range(inital_value, 100):
        print(step)
        inital_value += step_int
    Sum_of_series += inital_value
print("Sum of series: ", Sum_of_series)


#ÓKLARAÐ!!!!!!
