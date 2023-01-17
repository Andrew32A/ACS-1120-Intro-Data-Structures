import random

def random_sentence_generator():
    dictionary = open("/usr/share/dict/words", "r") # opens and reads dictionary on unix devices
    words = dictionary.read().split()
    dictionary.close()
    sentence = (random.sample(words, 5)) # randomly samples 5 words from dictionary
    print(" ".join(sentence)) # removes brackets and commas by combining items in array into a string

if __name__ == "__main__":
    random_sentence_generator()