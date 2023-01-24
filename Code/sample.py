import histogram
import random

source_text = "one fish two fish three fish four fish"

def sampler(histogram):
    '''
    returns one random word from histogram
    '''
    random_word = random.sample(histogram, 1)



if __name__ == "__main__":
    sample = sampler(histogram.histogram(source_text))

    print(sample)