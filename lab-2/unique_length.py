from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_REGEX = re.compile(r"\b\w+\b")


class UniqueLength(MRJob):
    def mapper_words(self, _, line):
        words = WORD_REGEX.findall(line)
        for word in words:
            yield (word.lower(), None)

    def reducer_unique(self, word, _):
        yield(word, None)

    def mapper_length(self, word, _):
        yield(len(word), 1)

    def reducer_sum(self, length, counts):
        yield(length, sum(counts))

    def steps(self):
        return [MRStep(mapper=self.mapper_words,
                       reducer=self.reducer_unique),
                MRStep(mapper=self.mapper_length,
                       reducer=self.reducer_sum)]


if __name__ == '__main__':
    UniqueLength.run()
