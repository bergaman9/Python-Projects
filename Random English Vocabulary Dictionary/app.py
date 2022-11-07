from PyDictionary import PyDictionary
import random

dictionary = PyDictionary()


def get_word():
    valid_word = False
    while(not valid_word):
        index = random.randint(0,190000)
        word = words[index]
        if(len(word) > 2):
            valid_word = True
            return word

# get definition of word
def define_word():
    valid_word = False
    while(not valid_word):
        word = get_word()
        if(dictionary.meaning(word, disable_errors=True)):
            print(word.upper()+"\n")
            defs = dictionary.meaning(word)
            for key, value in defs.items():
                print(str(key)+": "+ str(value).strip("[]\'\"").replace("\'", "")+"\n")

            valid_word = True


file = open("words.txt", "r")
words = file.read().split("\n")

define_word()
