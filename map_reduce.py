from functools import reduce
from pprint import pprint

def count_words(doc):
    normalized_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalized_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

documents = [
    'this is the information about the language that is being used very widely these days',
    'the public transport is very much underutilized these days as most poeple work from home',
    'current housing market is very much inflated and there are wories more than ever that it will end up in price crush'
]

counts = (map(count_words, documents))

def combine_counts(d1, d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d


total_counts = reduce(combine_counts, counts)

pprint(total_counts)
