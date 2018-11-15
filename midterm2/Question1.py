def get_file_name():
    file_name = input('File name: ')
    return file_name


def get_longest_word(file_stream):
    longest_word = ''
    for word in file_stream:
        word = word.strip()
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def open_file(file_name):
    file_stream = open(file_name, 'r')
    return file_stream

def main():
    file_name = get_file_name()
    file_stream = False
    while file_stream == False:
        file_name = get_file_name()
        try:
            file_stream = open_file(file_name)
        except:
            print("þessi fíll er ekki til staðar, því miður, NÆSTI!")

    longest_word = get_longest_word(file_stream)
    print("longest word is {} of lenght {}".format(longest_word, len(longest_word)))

main()