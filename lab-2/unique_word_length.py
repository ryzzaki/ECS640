from mrjob.job import MRJob
import re

WORD_REGEX = re.compile(r"\b\w+\b")


class UniqueLength(MRJob):
    def mapper(self, _, line):
        words = WORD_REGEX.findall(line)
        for word in words:
            yield (len(word), word.lower())

    def combiner(self, length, words):
        unique_words = set(words)
        for word in unique_words:
            yield (length, word)

    def reducer(self, length, words):
        unique_words = set(words)
        yield (length, len(unique_words))


if __name__ == '__main__':
    UniqueLength.run()
