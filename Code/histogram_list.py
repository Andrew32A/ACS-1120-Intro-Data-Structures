import sys

source_text = "one fish two fish three fish four fish"

count_storage = []
word_storage = []

histogram_storage = []

def histogram(source_text):
    split_text = source_text.split()

    for i in range(len(split_text) - 1):
        count_storage.append(1)
    
    for word in split_text:
        word_storage.append(word)

    for i in range(len(split_text) - 1):
        if split_text[i] in word_storage:
            count_storage[i] += 1

    for i in range (len(split_text) - 1):
        histogram_storage.append([split_text[i], count_storage[i]])

    print (histogram_storage)

# def unique_words(histogram):
#     '''
#     prints length of histogram
#     '''
#     print(f"There are {len(histogram)} unique words in the source text")

# def frequency(word, histogram):
#     '''
#     prints value of key that was put in as an argument
#     '''
#     try:
#         print(f"The word {word} appeared {histogram[word]} time(s) in the source text")
    
#     except:
#         print(f"The word {word} appeared 0 times in the source text")

if __name__ == "__main__":
    histogram(source_text)
    # unique_words(histogram_storage)
    # frequency(sys.argv[1].lower(), histogram_storage)

