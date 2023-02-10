from dictogram import Dictogram
from histogram import file_reader
import random

class MarkovChain():
    def __init__(self, source_text):
        self.source_text = source_text
        self.histogram = Dictogram(source_text)
        # self.starting_point = self.generate_starting_point()
        # self.ending_point = self.generate_ending_point()

    def generate_starting_point(self):
        return self.histogram.sample()

    def generate_ending_point(self):
        return self.histogram.sample()

    def build_map(self):
        words = self.source_text
        map = {}
        for i in range(len(words) - 1):
            next_word = words[i + 1]
            if words[i] in map:
                map[words[i]].append(next_word)
            else:
                map[words[i]] = [next_word]
        return map

    def generate_sentence(self):
        map = self.build_map()
        sentence = []
        sentence.append(self.generate_starting_point())
        next_word = self.generate_starting_point()
        count = 0

        for _ in range(20):
            count += 1
            next_word = random.choice(map[next_word])
            sentence.append(next_word)
            if next_word == self.generate_ending_point or count == 20:
                return " ".join(sentence).capitalize() + "."
                
if __name__ == "__main__":
    source_text = file_reader("./data/corpus.txt")
    markov = MarkovChain(source_text)
    print(markov.generate_sentence())

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