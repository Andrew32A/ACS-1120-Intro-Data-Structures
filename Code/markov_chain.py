from histogram import file_reader
import random

class MarkovChain():
    def __init__(self, source_text):
        self.source_text = file_reader(source_text) # text that is read from helper function and converted through re
        self.source_text_raw = source_text # raw text that's later broken down in read_source_text method

    def read_source_text(self, source_text_raw):
        '''
        takes raw text and splits into a list
        '''
        with open(str(source_text_raw)) as text:
            text = text.read()
            text = text.split()
        return text

    def generate_starting_point(self):
        '''
        generates a list of words that are capitalized then selects one as a starting point
        '''
        word_list = self.read_source_text(self.source_text_raw)
        starting_words = []
        for word in word_list:
            if word[0].isupper() == True:
                starting_words.append(word) 
        return random.choice(starting_words).lower()

    def generate_ending_point(self):
        '''
        generates a list of words that end in a period then selects one as an ending point
        '''
        word_list = self.read_source_text(self.source_text_raw)
        ending_words = []
        for word in word_list:
            if word[-1] == ".":
                ending_words.append(word) 
        return random.choice(ending_words).lower()

    def build_map(self):
        '''
        creates a dictionary where the key is a word, then the value is a list of the words that follow the key word
        '''
        words = self.source_text
        map = {}
        for i in range(len(words) - 1):
            next_word = words[i + 1]
            if words[i] in map:
                map[words[i]].append(next_word)
            else:
                map[words[i]] = [next_word]
        return map

    def generate_sentence(self, max_words):
        '''
        generates a sentence based on words following the starting point and ends on the ending point
        '''
        map = self.build_map()
        starting_point = self.generate_starting_point()
        ending_point = self.generate_ending_point()

        sentence = [starting_point]
        next_word = starting_point
        count = 0

        while True:
            count += 1
            # bandaid fix for when the next word has no value
            try:
                next_word = random.choice(map[next_word])
            except:
                return " ".join(sentence).capitalize() + f" {ending_point}"

            sentence.append(next_word)
            if next_word == ending_point or count == max_words:
                if count == max_words:
                    return " ".join(sentence).capitalize() + f" {ending_point}"
                else:
                    return " ".join(sentence).capitalize() + random.choice("..!?")
                
if __name__ == "__main__":
    source_text = "./data/shrek_corpus.txt"
    markov = MarkovChain(source_text)
    print(markov.generate_sentence(10))
