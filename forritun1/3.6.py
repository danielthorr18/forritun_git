c = 10

while c < 100:
    if (c**2) % 100 == c:
        print(c)
        break
    else:
        c+=1