import string
import operator

def get_word_list(filename):
    ''' Reads the given file and returns a list of lower case words.
        Punctuation at the start and end of a word are removed.
    '''
    all_words = []
    try:
        file = open(filename, 'r')
        for line in file:	# process each line
            line = line.strip() # strip leading and trailing white space
            word_list = line.split() # get a list of words in the line
            for word in word_list:
                word = word.lower()
                word = word.strip(string.punctuation) # remove punctuation
                all_words.append(word)
    
        file.close
    except FileNotFoundError:
        pass
    return all_words

def get_bigrams(word_list):
    ''' Creates a dictionary of bigrams from the given word_list.
        The keys are tuples of words that co-occur, the values are their occurances counts.
    '''
    bigrams = {}
    previous_word = ''
    for word in word_list:
        if previous_word != '':
            bigram = (previous_word, word)
            if bigram in bigrams:
                bigrams[bigram] += 1
            else:
                bigrams[bigram] = 1
        previous_word = word
    return bigrams

# The main program starts here

filename = input("Enter name of file: ")
all_words = get_word_list(filename)
if all_words:
    bigrams = get_bigrams(all_words)
    sorted_bigrams = sorted(bigrams.items(), key=operator.itemgetter(1,0), reverse=True)
    bigrams_top_10 = [ sorted_bigrams[i] for i in range(0,10)]
    print(bigrams_top_10)