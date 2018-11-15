vowels = 'aeiuo'
word = ''


''' if begins with con, remove all con from beginning of word until first vowel, append to end of word + 'ay'.'''
''' if begins with vow, append 'yay' to end of the word'''

while word != '.':
    word = input("Enter a word: ")
    if word[0].lower() in vowels:
        print(word + 'yay')

    else:
        conWord = ''
        for i in word:
            if i not in vowels:
                conWord += i
            else:
                print(word[len(conWord):] + conWord + 'ay')
                break

        else:
            print(word + 'ay')