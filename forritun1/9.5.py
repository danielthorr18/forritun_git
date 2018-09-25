with open("words.txt", "r") as words:
    with open("sentences.txt", "w") as sentences:
        sentence = ""
        for line in words:
            word = line.strip()
            if word == ".":
                sentence += word +" \n"
            elif word == "":
                sentence += ""
            else:
                sentence += word + " "
               
        print(sentence)