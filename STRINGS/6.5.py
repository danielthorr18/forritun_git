s = input("Input a string: ")

digit_row = ""

for digit in(s):
    if digit.isdigit():
        digit_row += digit
print(digit_row)
