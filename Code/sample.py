import histogram
import random

def sampler(histogram):
    '''
    returns one random word from histogram
    '''
    random_word = random.sample(list(histogram.items()), 1) # changed dict to a list to avoid deprecation warning "DeprecationWarning: Sampling from a set deprecated since Python 3.9 and will be removed in a subsequent version."

    return random_word

def probability(histogram):
    pass

if __name__ == "__main__":
    source_text = "one fish two fish three fish four fish"
    sample = sampler(histogram.histogram(source_text))

    print(f"Random sample result: {sample[0][0]}: {sample[0][1]}")