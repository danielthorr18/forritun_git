def list_to_tuple(my_list):
    my_tuple = ()
    for item in my_list:
        try:
            int_item = int(item)
            my_tuple += (int_item,)
        except:
            print("Error. Please enter only integers.")
            return()
    return my_tuple



# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)