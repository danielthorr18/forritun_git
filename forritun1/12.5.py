def game_of_eights(numbers):
    test = '1'
    for num in numbers:
        if num == '8' and num == test:
            return True
        test = num
    return False
    #game_of_eights() function goes here

def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    for stak in a_list:
        try:
            int(stak)
        except:    
            print("Error. Please enter only integers.")
            return
    print(game_of_eights(a_list))

main()