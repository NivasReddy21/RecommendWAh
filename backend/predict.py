import jieba
import pandas as pd
import numpy as np
from surprise import Reader, Dataset, SVD
from gensim.models import Word2Vec, KeyedVectors
import nltk
from gensim import corpora
from gensim.utils import simple_preprocess
import ignoreRep

model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300_1.bin', binary=True, limit=100000)

data = pd.read_csv("good_reads_final.csv")
data = data[["genre_1", "book_title", "book_fullurl"]]

genres = data.genre_1.unique()
genre_list = []

for genre in genres:
    genre_list.append(genre.lower())

ppg_list = model.wv.most_similar('programming')

reco_list = []

for i in ppg_list:
    reco_list.append(i[0].lower())

for word, count in ignoreRep.returnFreq().most_common(150):
        print(word, ": ", count)