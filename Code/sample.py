from histogram import dictogram
from histogram import file_reader
import random

def sampler(text_to_sample):
    '''
    returns one random word from histogram
    '''
    words_from_histogram = dictogram(text_to_sample)
    random_word = random.choices(
        list(words_from_histogram.keys()), 
        weights = words_from_histogram.values(),
        k = 1) [0] # changed dict to a list to avoid deprecation warning "DeprecationWarning: Sampling from a set deprecated since Python 3.9 and will be removed in a subsequent version."

    return random_word

def probability(source_text):
    '''
    takes in 10,000 samples and returns probability for each word
    '''
    repeats = {}
    
    for _ in range(10000):
        sampled_word = sampler(source_text)
        if sampled_word in repeats:
            repeats[sampled_word] += 1
        else:
            repeats[sampled_word] = 1

    return repeats

def sentence_generator(source_text, num_of_words):
    '''
    combines sampled words from source_text into a sentence
    '''
    word_list = []
    for _ in range(num_of_words):
        word_list.append(sampler(source_text))

    return " ".join(word_list).capitalize() + "."

if __name__ == "__main__":
    source_text = file_reader("./data/corpus.txt")

    sample = sampler(source_text)
    print(sample)

    probability_output = probability(source_text)
    for word in probability_output:
        print(f"{word}: {probability_output[word]}")

    print(sentence_generator(source_text, 10))