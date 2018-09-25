def is_float(s):
    try:
        s = float(s)
        return True
    except:
        return False
# is_float function definition goes here

# Do not change the lines below
print(is_float('3.45'))
print(is_float('3e4'))
print(is_float('abc'))
print(is_float('4'))
print(is_float('.5'))