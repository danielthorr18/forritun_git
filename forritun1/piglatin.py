serhljod = ['a', 'e', 'i', 'o', 'u']
keyra = True
while keyra:
    word = str(input("Enter a word: "))
    if word == '.':
        keyra = False
        break
    elif word[0] in serhljod:
        print(word + "yay") 
    elif word[1] in serhljod:
        print(word[1:] + word[0] + "ay")
    elif word[2] in serhljod:
        print(word[2:] + word[:2] + "ay")
    elif len(word) > 4:
        print(word[3:] + word[:3] + "ay")  
    else:
        for letter in serhljod:
            if word != serhljod:
                print(word + "ay")
                break
