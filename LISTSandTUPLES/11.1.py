
def mutate_list(a_list, index_num, v):
    ''' Inserts v at index index_num in a_list'''
    a_list.insert(index_num, v)
    
def remove_ch(a_list, index_num):
    ''' Removes character at index_num from a_list'''
    a_list.pop(index_num)
    
def get_list():
    ''' Reads in values for a list and returns the list '''
    user_list = input("Enter values in list separated by commas: ")
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    return user_list

# Main program starts here
new_value = get_list()
print(new_value)

choice = input("Enter choice (m,r): ")

if choice == "r":
    index = int(input())
    remove_ch(new_value, index)
elif choice == "m":
    my_input = input()
    my_split = my_input.split(",")
    mutate_list(new_value, int(my_split[0]), int(my_split[1]))

print(new_value)

