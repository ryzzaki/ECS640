"""
Change the Hadoop job so that instead of counting words it counts bigrams (pairs of consecutive words). You can use the format "word1, word2", encoded in a Text(String) object for the keys to be sent between the Mapper and Reducer.
Change the Hadoop job so that you compute the total counts of word length for the dataset. That is, the number of words appearing in the text of length 1, 2, 3, ...etc.; Take into account that in this case you should change the intermediate key value types, so that they are [IntWritable, IntWritable] instead of [Text, IntWritable]. You will need to modify all three Java files to update the data types completely in Hadoop. What is the most common word length? You can discover that by inspecting the file manually, or running a Unix command over the results of the job: sort -n -k2 part-00000 | tail . However, that option would not be feasible with a large dataset. Try to define a second MapReduce project for computing this, using the output folder of the first job as the input for the second.
"""
from mrjob.job import MRJob
import re

WORD_REGEX = re.compile(r"\b\w+\b")


class BiGram(MRJob):
    def mapper(self, _, line):
        words = WORD_REGEX.findall(line)
        if len(words) >= 2:
            word1 = words.pop(0).lower()
            for word in words:
                bigram = word1, word.lower()
                word1 = word
                yield (bigram, 1)

    def reducer(self, word, counts):
        yield (word, sum(counts))


if __name__ == '__main__':
    BiGram.run()
