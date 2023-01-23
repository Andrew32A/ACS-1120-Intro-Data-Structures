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

    for word, number in histogram_storage.items():
        print(f"{word}: {number}")

def unique_words(histogram):
    print(f"There are {len(histogram_storage)} unique words in the source text.")

def frequency(word, histogram):
    pass

if __name__ == "__main__":
    histogram(source_text)
    unique_words(histogram_storage)
    # frequency(sys.argv[1])