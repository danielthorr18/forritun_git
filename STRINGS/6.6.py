name = input("Input a name: ")
fyrsta, seinna = name.split(", ")

first_name = fyrsta[0:].title()

last_name = seinna[0].upper()


print((last_name) + ". " + (first_name))