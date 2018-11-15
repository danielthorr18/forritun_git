secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)
hours = secs_int//3600
rest = (secs_int%3600)
minutes = rest//60
rest2 = rest % 60
seconds = rest2
print(hours,":",minutes,":",seconds) # do not change this line
