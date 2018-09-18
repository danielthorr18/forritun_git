def find_min(num1, num2):
    if num1 < num2:
        return(num1)
    else:
        return(num2)        # find_min function definition goes here
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

minimum = find_min(first, second)
    
# Call the function here
print("Minimum: ", minimum)