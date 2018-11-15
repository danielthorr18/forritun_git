"""Write a program that:

Reads in two lists of integers from the user and converts them to sets and prints out the sets.
Allows the user to repeatedly perform intersection, union and difference on the two sets and prints out the result of each operation
Example input/ouput:

Input a list of integers separated with a comma: 1,2,3,4
Input a list of integers separated with a comma: 1,1,3,3,5,6
{1, 2, 3, 4}
{1, 3, 5, 6}
1. Intersection
2. Union
3. Difference
4. Quit
Set operation: 1
{1, 3}"""
def intersection_func(listi1_set, listi2_set):
    print(listi1_set & listi2_set)

def union_func(listi1_set, listi2_set):
    print(listi1_set | listi2_set)

def difference_func(listi1_set, listi2_set):
    print(listi1_set - listi2_set)

def choice(listi1_set, listi2_set):
    q = True
    while q:
        print("1. Intersection\n2. Union\n3. Difference\n4. Quit")
        choose = input("Set operation: ")
        if choose == "1":
            intersection_func(listi1_set, listi2_set)
        elif choose == "2":
            union_func(listi1_set, listi2_set)
        elif choose == "3":
            difference_func(listi1_set, listi2_set)
        elif choose == "4":
            q = False

def list_to_int(listi):
    listi_tomur = []
    for i in listi:
        x = int(i)
        listi_tomur.append(x)
    return listi_tomur


def get_list():
    listi1 = input("Input a list of integers separated with a comma: ").split(",")
    listi2 = input("Input a list of integers separated with a comma: ").split(",")

    listi1_int = list_to_int(listi1)
    listi2_int = list_to_int(listi2)
    return listi1_int, listi2_int

def main():
    listi1_int, listi2_int = get_list()
    listi1_set = set(listi1_int)
    listi2_set = set(listi2_int)

    print(listi1_set)
    print(listi2_set)
    choice(listi1_set, listi2_set)

main()