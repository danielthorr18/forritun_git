
def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def get_integer(prompt):
    val = int(input(prompt))
    return val

def transform(list1, list2, r1, r2):
    empty_list = []
    for num in range(r1, r2):
        empty_list.append(list1[num])
    for num in empty_list:
        list1.remove(num)
    empty_list.reverse()
    list2 += empty_list



# Main program starts here - DO NOT change it
list1 = get_list()
list2 = get_list()
index1 = get_integer("Enter from value: ")
index2 = get_integer("Enter to value: ")
transform(list1, list2, index1, index2)
print(list1)
print(list2)