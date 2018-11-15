import random
import string

def get_word_string(filename):
    try:
        with open(filename, 'r') as dataFile:
            wordString = '' # start with an empty string of words
            for line in dataFile:
                wordString += line # add each line of words to the word string
                words = wordString.split()
                return(words)
    except FileNotFoundError:
        print("file not found try again!")


def scramble_string(word_string):
    tomur_listi = []
    midjan = ""
    for word in word_string:
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
scrambled_string = scramble_string(word_string)
print(scrambled_string)