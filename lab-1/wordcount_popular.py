"""
Lab 1. Wordcount with popular words
"""
from mrjob.job import MRJob
import re

WORD_REGEX = re.compile(r"\b\w+\b")


class Counter(MRJob):
    def mapper(self, _, line):
        words = WORD_REGEX.findall(line)
        for word in words:
            yield (word.lower(), 1)

    def reducer(self, word, counts):
        total = sum(counts)
        if total >= 10:
            yield (word, total)


if __name__ == '__main__':
    Counter.run()
