"""Design a class called Sentence that has a constructor that takes a string representing the sentence as input.  
The class should have the following methods:

get_first_word(): returns the first word as a string
get_all_words(): returns all words in a list.
replace(index, new_word): Changes a word at a particular index to "new_word".  
For example, if sentences is "I'm going back", then replace(2, "home") results in "I'm going home".  
If the index is not valid, the method does not do anything."""

class Sentence:
    def __init__(self, sentence=""):
        self.sentence = sentence
        self.list = sentence.split()


    def get_first_word(self):
        return self.list[0]
    
    def get_all_words(self):
        return self.list

    def replace(self, index, new_word):
        try:
            self.list[index] = new_word
        except:
            pass

sent = Sentence('Here we have a longer sentence')
print(sent.get_first_word())
print(sent.get_all_words())
sent.replace(2, "find")
print(sent.get_all_words())
sent.replace(10,"bla")
print(sent.get_all_words())