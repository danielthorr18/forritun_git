def enter_data(a_dict):
    name = input("Name: ")
    number = input("Number: ")

    a_dict[name] = number

def more_data():
    more = input("More data (y/n)? ")
    return more.lower() == 'y'

def dict_to_tuples(the_dict):
    dictlist = []
    for key, value in the_dict.items():
        temp = (key, value)
        dictlist.append(temp)
    return dictlist

def main():
    the_dict = {}
    go_again = True
    while go_again:
        enter_data(the_dict)
        go_again = more_data()

    dictlist = dict_to_tuples(the_dict)
    print(sorted(dictlist))

main()