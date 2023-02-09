from dictogram import Dictogram
from histogram import file_reader
import random

#  select starting point, capitalized word or most common word
source_text = file_reader("./data/corpus.txt")
# source_text = "one fish two fish three fish four fish"
histogram = Dictogram(source_text)

starting_point_picker = histogram.sample()

# create map from histogram, key = word, value = list of common words after it
def build_map(source_text):
    words = source_text
    histogram = {}
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]
        if word in histogram:
            histogram[word].append(next_word)
        else:
            histogram[word] = [next_word]
    return histogram

def map_sample(histogram, word):
    next_words = histogram[word]
    return random.choice(next_words)

def generate_sentence(histogram, start_word):
    sentence = [start_word]
    word = start_word
    while word in histogram:
        next_word = map_sample(histogram, word)
        sentence.append(next_word)
        word = next_word
    return " ".join(sentence)

# # generate sentence
# def generate_sentence(starting_point, words):
#     sentence = []
#     sentence.append(starting_point)

#     for _ in range(words):
#         # add word picker function here
#         sentence.append("arg for word picker here")

#     return sentence

# print(generate_sentence(starting_point_picker, 10))

print(build_map(source_text))