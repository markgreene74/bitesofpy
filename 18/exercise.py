import os
import urllib.request
import re
from collections import Counter

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)

pattern = re.compile('\W+')

def get_words(text):
    for line in text:
        for word in line.split():
            yield pattern.sub('', word.lower())

def get_harry_most_common_word():
    with open(stopwords_file) as f:
        stopwords = f.readlines()
    with open(harry_text) as f:
        text = f.readlines()
    nowords = list(get_words(stopwords))
    c = Counter(get_words(text))
    for item in c.most_common():
        if not item[0] or item[0] in nowords:
            continue
        else:
            return item