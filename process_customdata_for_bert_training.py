from nltk.tokenize import sent_tokenize
from tqdm import tqdm
import pandas as pd
import argparse


def create_corpus(corpus_path, output_path):
    corpus = pd.read_csv(corpus_path, sep='\t')
    corpus.reset_index(drop=True, inplace=True)
    article_corpus = open(output_path, "w")
    for i, row in tqdm(corpus.iterrows(), total=len(corpus)):
        article = row['text']
        article = article.strip()
        article2sentlist = sent_tokenize(article)
        if len(article2sentlist) >= 20:
            for sent in article2sentlist[2:20]:
                sent = sent.strip()
                if len(sent) <= 1: continue
                article_corpus.write(sent + "\n")
        else:
            for sent in article2sentlist:
                sent = sent.strip()
                if len(sent) <= 1: continue
                article_corpus.write(sent + "\n")
        # need "\n" to split diff articles
        article_corpus.write("\n")
    article_corpus.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--corpus_path', type=str, required=True)
    parser.add_argument('--output_path', type=str, required=True)
    args = parser.parse_args()
    create_corpus(args.corpus_path, args.output_path)
