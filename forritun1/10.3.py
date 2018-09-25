def populate_list(initial_list):
    my_input = input("Enter value to be added to list: ")
    while my_input.lower() != 'exit':
        initial_list.append(my_input)
        my_input = input("Enter value to be added to list: ")                                # Your functions should appear here
def triple_list(listinn_minn):
    
    return listinn_minn*3
    

# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)