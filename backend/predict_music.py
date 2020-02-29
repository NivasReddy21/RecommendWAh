import pandas as pd
import collections
from gensim.models import Word2Vec, KeyedVectors
import nltk
from gensim.utils import simple_preprocess
import ignoreRep
from nltk.corpus import stopwords

model = KeyedVectors.load_word2vec_format('trained_data.bin', binary=True, limit=100000)

data = pd.read_csv("Databases/music.csv")
data = data[["terms", "title", "artist.name"]]

genres = data.terms.unique()
genre_list = []


for genre in genres:
    genre_list.append(genre)

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

counter = []
completedReco = []

for reco in recommendation:
    word_counter = collections.Counter(recommendation)

for word, count in word_counter.most_common(100):
        completedReco.append(word)

print(completedReco)