def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True

def find_max(n):

    value = 0
    if value > max_number:
        max_number = value
    return max_number

def find_min(n):

    value = min_number
    if value < min_number:
        min_number = value
    return min_number

def find_average(n):
    average_number = sum(n)/len(n)
    return average_number

def create_myList(n):
    my_list = []
    n = input("Enter integers separated with commas: ").split(",")
    my_list.append(n)
    return my_list

def main(n):
    input_list = create_myList(n)
    print("Input list: ").format(input_list)
    
    prime_numbers = is_prime(input_list)
    print("Prime list: {}").format(prime_numbers)
    
    
    sorted_list = sorted(input_list)
    print("Sorted list: {}").format(sorted_list)
    
    max_number = find_max(input_list)
    min_number = find_min(input_list)
    average_number = find_average(input_list)
    print("Min: {}, Max: {}, Average: {}").format(min_number, max_number, average_number)


main()






