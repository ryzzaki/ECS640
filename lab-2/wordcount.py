"""
Wordcount script with Combiner
"""
from mrjob.job import MRJob
import re

WORD_REGEX = re.compile(r"\b\w+\b")


class Counter(MRJob):
    def mapper(self, _, line):
        words = WORD_REGEX.findall(line)
        for word in words:
            yield (word.lower(), 1)

    def combiner(self, word, counts):
        yield (word, sum(counts))

    def reducer(self, word, counts):
        # sum is a generator function - must be saved in a total variable as we can call it only once
        total = sum(counts)
        if total >= 10:
            yield (word, total)


if __name__ == '__main__':
    Counter.JOBCONF = {'mapreduce.job.reduces': '4'}
    Counter.run()
