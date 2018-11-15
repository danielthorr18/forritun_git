
def count_case(my_string):
    
    uppercount = 0
    lowercount = 0
    for item in (my_string):
        if str.isupper(item):
            uppercount = uppercount + 1               
        elif str.islower(item):
            lowercount = lowercount + 1

    return uppercount, lowercount

user_input = input("Enter a string: ")

uppercount, lowercount = count_case(user_input)


print("Upper case count: ", uppercount)
print("Lower case count: ", lowercount)