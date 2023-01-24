import sys
import re

def histogram(source_text):
    '''
    splits source text into separate items then adds 1 to the key's value if repeated then prints result
    '''
    histogram_storage = {}
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

    # for word, number in histogram_storage.items():
    #     print(f"{word}: {number}")

    return histogram_storage

def listogram(source_text):
    """
    same has histogram function, but uses a list instead
    """
    listogram = []
    temp_list = []
    list_of_words = re.findall(r"\w+", source_text.lower())
    for word in list_of_words:
        if word not in temp_list:
            listogram.append([word, list_of_words.count(word)])
            temp_list.append(word)

    return listogram

def unique_words(histogram):
    '''
    prints length of histogram
    '''
    return (f"There are {len(histogram)} unique words in the source text")

def frequency(word, histogram):
    '''
    prints value of key that was put in as an argument
    '''
    try:
        return (f"The word {word} appeared {histogram[word]} time(s) in the source text")
    
    except:
        return (f"The word {word} appeared 0 times in the source text")

if __name__ == "__main__":
    source_text = "one fish two fish three fish four fish"

    print(histogram(source_text))
    print(listogram(source_text))
    print(unique_words(histogram(source_text)))
    print(frequency(sys.argv[1].lower(), histogram(source_text)))

