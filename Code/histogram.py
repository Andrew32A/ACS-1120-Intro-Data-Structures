import sys

source_text = "one fish two fish three fish four fish"
histogram_storage = {}

def histogram(source_text):
    split_text = source_text.split()
    for word in split_text:
        if word in histogram_storage:
            histogram_storage[word] += 1
        else:
            histogram_storage[word] = 1

    print (histogram_storage)

def unique_words():
    pass

def frequency():
    pass

if __name__ == "__main__":
    histogram(source_text)