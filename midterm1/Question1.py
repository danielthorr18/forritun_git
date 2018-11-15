month = input('input a month: ').lower()
day = int(input('input a date: '))

full_date = '{} {}'.format(month.capitalize(), day)
print(full_date)

if full_date == 'January 1':
    print("New year's day")
elif full_date == 'June 17':
    print("National holiday")
elif full_date == 'December 25':
    print("Christmas day")
else:
    print("this is not a holiday mandem")