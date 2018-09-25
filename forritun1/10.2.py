
def to_list(string):
    if ',' in string:
        return string.split(",")
    return string.split(" ")



the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)