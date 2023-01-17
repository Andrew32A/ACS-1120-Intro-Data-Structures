import random
import sys

def rearranger():
    words = sys.argv.copy()
    words.pop(0) # have to remove the first item in array because it copies "rearrance.py" too
    return words

if __name__ == "__main__":
    print(random.sample(rearranger(), len(rearranger())))