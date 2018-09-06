s = input("Input a string: ")

find =  s.find("o")
for item, o in enumerate(s):
    if "o" == o:
        print(item)
