def get_word_list(fpointer):
    my_list = []
    word_list = []
    for line in fpointer:
        my_list += line.split()
    for item in my_list:
        item = item.strip(",").strip("\n").strip(".").lower()
        word_list.append(item)
    return word_list

def  word_list_to_counts(word_list):
    a_dict = {}
    for word in word_list:
        if word not in a_dict:
            a_dict[word] = 1
        else:
            a_dict[word] += 1
    return a_dict
def dict_to_tuple(word_count_dict):
    return [(key,value) for key, value in word_count_dict.items()]    



def main():
    filename = input("Name of file: ")
    # Get a file pointer
    fpointer = open(filename)
    # Get a list of words from the file
    word_list = get_word_list(fpointer) 
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))
    
main()