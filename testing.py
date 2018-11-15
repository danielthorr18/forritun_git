import random
import string

def get_word_string(filename):
    try:
        with open(filename, "r") as read_file:
            strengur = ""
            for line in read_file:
                strengur += line
            strengur = strengur.split()
            return strengur
    except:
        print("File " + filename + " not found")

def scramble_string(word_string):
    tomur_listi = []
    midjan = ""
    for word in word_string:
        print(word)
        if len(word) >= 4:
            fyrsti = word[0]
            sidasti = word[-1]
            midjan = list(word[1:-1])
            if word[-1] in string.punctuation:
                sidasti = word[-2:]
                midjan = list(word[1:-2])
            random.shuffle(midjan)
            midjan = ''.join(midjan)
            nytt_ord = fyrsti + midjan + sidasti
            tomur_listi.append(nytt_ord)
        elif len(word) <= 3:
            tomur_listi.append(word)
        strengur = " ".join(tomur_listi)
    return strengur

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
print(word_string)
scrambled_string = scramble_string(word_string)
print(scrambled_string)