import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY, 'r') as f:
        content = f.readlines()
    word_list = []
    for i in content:
        word_list.append(i.strip('\n'))
    return word_list


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    thescore = 0
    for aletter in word.strip('\n'):
        thescore += LETTER_SCORES[aletter.upper()]
    return thescore


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    max_score = 0
    bestword = ''
    for singleword in words:
        singleword_score = calc_word_value(singleword)
        if singleword_score > max_score:
            max_score = singleword_score
            bestword = singleword
    return bestword