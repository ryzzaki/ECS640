## Setup

Follow the root `README.md` for the initial setup.

The dataset `sherlock.txt` contains all the data we will be working with.

The `results` folder contains all the output files.

## BiGram

```bash
python3 bigram.py sherlock.txt > ./results/out_bigram.txt

# using hadoop
python3 bigram.py -r hadoop hdfs://studoop.eecs.qmul.ac.uk/<user>/fcuadrado/sherlock.txt > ./results/out_bigram.txt
```

## Word Count

```bash
python3 wordcount.py sherlock.txt > ./results/out_wordcount.txt

# using hadoop
python3 wordcount.py -r hadoop hdfs://studoop.eecs.qmul.ac.uk/<user>/fcuadrado/sherlock.txt > ./results/out_wordcount.txt
```

## Word Count Popular

```bash
python3 wordcount_popular.py sherlock.txt > ./results/out_wordcount_popular.txt

# using hadoop
python3 wordcount_popular.py -r hadoop hdfs://studoop.eecs.qmul.ac.uk/<user>/fcuadrado/sherlock.txt > ./results/out_wordcount_popular.txt
```
