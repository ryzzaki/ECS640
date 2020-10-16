## Wordcount

```bash
python3 wordcount.py -r hadoop --output-dir out --no-cat-output hdfs://data/gutenberg
```

## Unique Word Length

Find out for each word length => how many unique words appear in the text corpora for each word size

```bash
python3 unique_word_length.py -r hadoop --output-dir out --no-cat-output hdfs://data/gutenberg
```
