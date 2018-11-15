def sort_list(a_list):
    a_list.sort()

    
def main():
    a_list = []
    while True:
        number = input()
        try:
            a_list.append(int(number))
        except ValueError:
            break


    #loop to accept integers until a non-digit is entered goes here
    
    
    
    ######Do not modify this part######
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    ######Do not modify this part######
    
main()