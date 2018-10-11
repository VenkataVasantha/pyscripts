#!/usr/bin/env python3

import sys
import re

def count_words():

    # final structure to be returned
    # Holds count for each word
    distinct_words = {}

    # read the stream of strings we receive
    # from the input
    for line in sys.stdin:
        # Each line we split into words
        for word in line.split():
            # remove special characters if the word has
            clean_word = re.sub(r'\W+', '', word)
            # convert all chars to lowercase
            lower_word = clean_word.lower()
            # add to the final structure
            distinct_words[lower_word] = distinct_words.get(lower_word, 0) + 1
    
    # sorting the final structure by descending order of word frequency
    sorted_words = sorted(distinct_words.items(), key=lambda x: x[1], reverse=True)

    # print the words and their counts
    for word, count in sorted_words:
        print(word, count)

if __name__ == "__main__":
    count_words()
