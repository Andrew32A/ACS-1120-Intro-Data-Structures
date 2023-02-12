from dictogram import Dictogram
from histogram import file_reader
import random

class MarkovChain():
    def __init__(self, source_text, source_text_raw):
        self.source_text = source_text
        self.source_text_raw = source_text_raw
        self.histogram = Dictogram(source_text)

    def read_source_text(self, source_text_raw):
        with open(str(source_text_raw)) as text:
            text = text.read()
            text = text.split()
        return text

    def generate_starting_point(self):
        word_list = self.read_source_text(self.source_text_raw)
        starting_words = []
        for word in word_list:
            if word[0].isupper() == True:
                starting_words.append(word) 
        return random.choice(starting_words).lower()

    def generate_ending_point(self):
        word_list = self.read_source_text(self.source_text_raw)
        ending_words = []
        for word in word_list:
            if word[-1] == ".":
                ending_words.append(word) 
        return random.choice(ending_words).lower()

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
        starting_point = self.generate_starting_point()
        ending_point = self.generate_ending_point()

        sentence = [starting_point]
        next_word = starting_point
        count = 0

        while True:
            count += 1
            next_word = random.choice(map[next_word])
            sentence.append(next_word)
            if next_word == ending_point or count == 10:
                if count == 10:
                    return " ".join(sentence).capitalize() + f" {ending_point}"
                else:
                    return " ".join(sentence).capitalize() + random.choice("..!?")
                
if __name__ == "__main__":
    source_text_read = file_reader("./data/shrek_corpus.txt")
    source_text_raw = "./data/shrek_corpus.txt"
    markov = MarkovChain(source_text_read, source_text_raw)
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