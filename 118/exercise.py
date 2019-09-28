from collections import defaultdict

def get_duplicate_indices(words):
    """Given a list of words, loop through the words and check for each
       word if it occurs more than once.
       If so return the index of its first ocurrence.
       For example in the following list 'is' and 'it'
       occurr more than once, and they are at indices 0 and 1 so you would
       return [0, 1]:
       ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
       Make sure the returning list is unique and sorted in ascending order."""
    all_words = defaultdict(list)
    for position, word in enumerate(words):
        all_words[word].append(position)
    return [x[0] for x in all_words.values() if len(x) > 1]
