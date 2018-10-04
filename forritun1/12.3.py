import string
def build_wordlist(infile):
    word_list = []
    for word in infile:
        if word not in string.punctuation:
            word = word.strip().split()
            word_list += word
       
    return word_list
    #build_wordlist() function goes here

def find_unique(word_list):
    new_wordlist = []
    for word in word_list:
        if word not in new_wordlist:
            new_wordlist.append(word)
    return new_wordlist

def main():
    infile = open("forritun1/test.txt", 'r')
    word_list = build_wordlist(infile)  
    infile.close()  
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()