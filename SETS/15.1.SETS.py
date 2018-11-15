"""Write a program that prompts the user for a name.  The program then splits the name into first and last name (case insensitive).

Then it:

calls a function that returns a list of the common letters in first and last. The data structures used in this implementation can only be lists.
calls a function that returns a set containing the common letters in first and last.  The data structures used in this implementation can only be sets.
prints out a sorted list version of the results from 1) and 2)
Example input/output:

 

Enter name: Barak Obama
['a', 'b']
['a', 'b']"""

def common_letters_list(first, last):
    common_letters = []      
    for letter in first:
        if letter in last and letter not in common_letters:
            common_letters.append(letter)
    return common_letters

def main():
    name = input("Enter name: ")
    first, last = name.lower().split()
    common_letters = common_letters_list(first,last)
    print(sorted(common_letters))
    print(sorted(common_letters))
    

main()