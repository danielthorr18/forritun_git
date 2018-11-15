def palindrome(setning):
    empty_string = ''
    for item in setning:
        if item.isalpha():
            empty_string += item
    empty_string = empty_string.lower()
    reverse = empty_string[::-1]
    if empty_string != reverse:
        return False
    else:
        return True


in_str = input("Enter a string: ")

setning = palindrome(in_str)
if setning:
    print(f'"{in_str}" is a palindrome.')
else:
    print(f'"{in_str}" is not a palindrome.')