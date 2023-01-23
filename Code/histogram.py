import sys

source_text = "one fish two fish three fish four fish"
histogram_storage = {}

def histogram(source_text):
    '''
    splits source text into separate items then adds 1 to the key's value if repeated then prints result
    '''
    split_text = source_text.split()
    for word in split_text:
        word = word.lower()
        if word[0].isalpha() == False: # skips non alphabetical strings by checking first index in string
            pass
        else:
            if word in histogram_storage:
                histogram_storage[word] += 1
            else:
                histogram_storage[word] = 1

    for word, number in histogram_storage.items():
        print(f"{word}: {number}")

def unique_words(histogram):
    '''
    prints length of histogram
    '''
    print(f"There are {len(histogram)} unique words in the source text")

def frequency(word, histogram):
    '''
    prints value of key that was put in as an argument
    '''
    try:
        print(f"The word {word} appeared {histogram[word]} time(s) in the source text")
    
    except:
        print(f"The word {word} appeared 0 times in the source text")

if __name__ == "__main__":
    histogram(source_text)
    unique_words(histogram_storage)
    frequency(sys.argv[1].lower(), histogram_storage)

