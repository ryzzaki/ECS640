from mrjob.job import MRJob
import re


class Counter(MRJob):
    def mapper(self, _, line):
        count = int(line.replace(" ", "").split('"').pop())
        yield ('total', count)

    def reducer(self, word, counts):
        yield (word, sum(counts))


if __name__ == '__main__':
    Counter.run()
