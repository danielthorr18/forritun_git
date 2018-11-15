"""add_to_dict(): takes a dictionary, a key, a value and adds the key,value pair to the dictionary. If key is already in dictionary then it displays the error message: "Error. Key already exists.". 
remove_from_dict(): takes a dictionary and key and removes the key from the dictionary.  If no such key is found in the dictionary then it prints: "No such key exists in the dictionary."
find_key(): takes dictionary and key and prints the value corresponding to the key from the dictionary: print("Value: ", value). If key is not found, then prints: "Key not found." """
def menu_selection():
    print("Menu: ")
    selection = "arf"
    choice = input("add(a), remove(r), find(f): ")
    if choice.lower() not in selection:
        print("Invalid choice.")
    else:
        return choice

def add_to_dict(a_dict):
    key = input("Key: ")
    value = input("Value: ")
    if key not in a_dict.keys():
        a_dict[key] = value
    else:
        print("Error. Key already exists.")

def remove_from_dict(a_dict):
    remove = input("key to remove: ")
    try:
        a_dict.pop(remove)
    except:
        print("No such key exists in the dictionary.")

def find_key(a_dict):
    find_key = input("Key to locate: ")
    if find_key in a_dict.keys():
        print("Value: ", a_dict[find_key])
    else:
        print("Key not found.")


def execute_selection(choice, a_dict):
    if choice == "a":
        add_to_dict(a_dict)
    elif choice == "r":
        remove_from_dict(a_dict)
    elif choice == "f":
        find_key(a_dict)

def dict_to_tuples(a_dict):
    return [(key, value) for key, value in a_dict.items()]

# Do not change this main function
def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()