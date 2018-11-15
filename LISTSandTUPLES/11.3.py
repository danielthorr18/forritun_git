
def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def even_sum(numbers):
    sum_of_even = [int(num) for num in numbers if int(num) % 2 == 0]
    return sum(sum_of_even)



# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
