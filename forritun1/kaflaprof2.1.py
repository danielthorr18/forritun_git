def get_longest_word(file_stream):
    longest_word = ""
    with file_stream as file:
        for word in file:
            if len(word) > len(longest_word):
                longest_word = word
        return longest_word.strip()

def open_file(filename):
    try:
        return open(filename, "r")
    except FileNotFoundError:
        return None


filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
    longest_word = get_longest_word(file_stream)
    print ("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
    file_stream.close
else:
    print('File',filename,'not found!')