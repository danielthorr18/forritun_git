name_month = input("Month: ")
number_day = input("Day: ")

date_str = name_month.capitalize() + number_day

if date_str == "January" + "1":
    print("New year's day", end = " ")
elif date_str == "June"  + "4":
    print("National holiday", end = " ")
elif date_str == "December" + "25":
    print("Christmas day", end = " ")
else:
    print("Not a holiday")
