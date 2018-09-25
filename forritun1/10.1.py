import string

sentence = input("Input a sentence: ")
unique_letters = []

for letter in sentence:
    if letter.isalpha():
        if letter not in unique_letters:

            unique_letters.append(letter)

print("Unique letters:", unique_letters)
