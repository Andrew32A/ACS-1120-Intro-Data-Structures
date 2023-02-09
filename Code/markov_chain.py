from dictogram import Dictogram
from histogram import file_reader
import random

class MarkovChain():
    def __init__(self):
        self.source_text = file_reader("./data/corpus.txt")
        self.histogram = Dictogram(self.source_text)
        self.starting_point_picker = self.histogram.sample()

    def build_map(self, source_text):
        words = source_text
        map = {}
        for i in range(len(words) - 1):
            next_word = words[i + 1]
            if words[i] in map:
                map[words[i]].append(next_word)
            else:
                map[words[i]] = [next_word]
        return map

    def generate_sentence(self, words, starting_point, source_text):
        map = self.build_map(source_text)
        sentence = []
        sentence.append(starting_point)
        next_word = starting_point

        for _ in range(words):
            word = next_word
            next_word = random.choice(map[word])
            sentence.append(next_word)

        return " ".join(sentence).capitalize() + "."


if __name__ == "__main__":
    markov = MarkovChain()
    print(markov.generate_sentence(20, markov.starting_point_picker, markov.source_text))

# ***** non-oop version *****

# # select starting point, capitalized word or most common word
# source_text = file_reader("./data/corpus.txt")
# histogram = Dictogram(source_text)

# starting_point_picker = histogram.sample()

# # create map from histogram, key = word, value = list of common words after it
# def build_map(source_text):
#     words = source_text
#     map = {}
#     for i in range(len(words) - 1):
#         next_word = words[i + 1]
#         if words[i] in map:
#             map[words[i]].append(next_word)
#         else:
#             map[words[i]] = [next_word]
#     return map

# # generate sentence
# def generate_sentence(words, starting_point, source_text):
#     map = build_map(source_text)
#     sentence = []
#     sentence.append(starting_point)
#     next_word = starting_point

#     for _ in range(words):
#         word = next_word
#         next_word = random.choice(map[word])
#         sentence.append(next_word)

#     return " ".join(sentence).capitalize() + "."

# if __name__ == "__main__":
    # print(generate_sentence(20, starting_point_picker, source_text))