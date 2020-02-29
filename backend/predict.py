import pandas as pd
from gensim.models import Word2Vec, KeyedVectors
import nltk
from gensim.utils import simple_preprocess
import ignoreRep
from nltk.corpus import stopwords

model = KeyedVectors.load_word2vec_format(
    'GoogleNews-vectors-negative300_1.bin', binary=True, limit=100000)

data = pd.read_csv("good_reads_final.csv")
data = data[["genre_1", "book_title", "book_fullurl"]]

genres = data.genre_1.unique()
genre_list = []


for genre in genres:
    genre_list.append(genre.lower())

word_list = []

for word, count in ignoreRep.returnFreq().most_common(10000):
    if word not in stopwords.words('english') and word.isalpha() and word not in word_list:
        word_list.append(word)


recommendation = []

for word1 in word_list:
    try:
        ppg_list = model.wv.most_similar(word1)
        for predict in ppg_list:
            if predict[0].lower() in genre_list:
                recommendation.append(predict[0].lower())

    except KeyError:
        pass

print(stopwords.words('english'))

counter = []

for word, count in ignoreRep.returnFreq().most_common(150):
    if word not in stopwords.words('english'):
        counter.append(count)
        print(word + ':' + str(count))
