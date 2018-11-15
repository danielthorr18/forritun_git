def sub_lists(my_list): 
    sublist = [[]]  
    for value1 in range(len(my_list) + 1):      
        for value2 in range(value1 + 1, len(my_list) + 1): 
            sub = my_list[value1:value2] 
            sublist.append(sub)   
    return sublist 

def main():

    my_list = input("Enter a list separated with commas: ").split(",")
    print(sub_lists(my_list))

main()
