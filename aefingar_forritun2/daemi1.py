def create_a_list(size):
    numbers = []
    while size > 0:
        value = input("Input value to list: ")
        size -= 1
        numbers.append(value)
    return numbers

def main():
    size = int(input("Enter size of list: "))
    my_list = create_a_list(size)
    print(my_list)





main()


