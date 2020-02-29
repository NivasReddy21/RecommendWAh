import collections
import pandas as pd
import matplotlib.pyplot as plt

def returnFreq():

    # Read input file, note the encoding is specified here 
    # It may be different in your text file
    file = open('data1.txt', encoding="utf8")
    a= file.read()
    # Stopwords
    stopwords = set(line.strip() for line in open('stopwords.txt'))
    stopwords = stopwords.union(set(['mr','mrs','one','two','said','a','the']))
    # Instantiate a dictionary, and for every word in the file, 
    # Add to the dictionary if it doesn't exist. If it does, increase the count.
    wordcount = {}
    # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
    for word in a.lower().split():
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("â€œ","")
        word = word.replace("â€˜","")
        word = word.replace("*","")
        if word not in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    
    # n_print = int(input("How many most common words to print: "))
    n_print = 150
    #print("\nOK. The {} most common words are as follows\n".format(n_print))
    word_counter = collections.Counter(wordcount)
    # for word, count in word_counter.most_common(n_print):
    #     print(word, ": ", count)
    
    file.close()

    return word_counter
    
returnFreq()