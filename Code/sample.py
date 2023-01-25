import histogram
import random
import re

def sampler(text_to_sample):
    '''
    returns one random word from histogram
    '''
    random_word = random.sample(list(text_to_sample.items()), 1) # changed dict to a list to avoid deprecation warning "DeprecationWarning: Sampling from a set deprecated since Python 3.9 and will be removed in a subsequent version."

    return random_word

def probability(source_text):
    repeats = {}
    words = []

    for i in range(10000):
        sampled_word = sampler(histogram.histogram(source_text))
        sampled_word = sampled_word[0][0]
        words.append(sampled_word)
        repeats[words[i]] = words.count(words[i])

    return repeats


if __name__ == "__main__":
    source_text = "one fish two fish three fish four fish"

    sample = sampler(histogram.histogram(source_text))
    print(f"Random sample result: {sample[0][0]}: {sample[0][1]}")

    probability_output = probability(source_text)
    print (probability_output)