skra = open("words.txt", "r")
lengsta = ""
for word in skra:
    word = str(word.replace("\n", ""))
    if len(word) > len(lengsta):
        lengsta = word
    
print("Longest word is '{}' of length {}".format(lengsta, len(lengsta)))