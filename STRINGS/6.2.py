s = input("Input a string: ")
three_letters = s[0:3]

s = s[3:] + (three_letters)
print(s)