import random
import sys

def random_sentence_generator(words_requested = 5):
    dictionary = open("/usr/share/dict/words", "r") # opens and reads dictionary on unix devices
    words = dictionary.read().split()
    dictionary.close()
    sentence = (random.sample(words, words_requested)) # randomly samples words from dictionary, defaults to 5
    print(" ".join(sentence)) # removes brackets and commas by combining items in array into a string then prints

if __name__ == "__main__":
    random_sentence_generator(int(sys.argv[1]))