import numpy as np
import nltk
#import spacy
from nltk.stem import SnowballStemmer
#sp_tokenizer = spacy.load('es_core_news_sm')
stemmer = SnowballStemmer('spanish')


def tokenize_es_1(sentence):
    tokens_en = nltk.word_tokenize(sentence)
    tokens_es = []
    for word in tokens_en:
        if word.startswith('¡') or word.startswith('¿'):
            tokens_es.append(word[0])
            tokens_es.append(word[1:])
        else:
            tokens_es.append(word)
    return tokens_es

#def tokenize_es_2(sentence):
    #tokenize = sp_tokenizer(sentence)
    #tokens = [str(token) for token in tokenize]
    #return tokens


def stem_es(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    # Setam each word of the sentence
    sentence_words = [stem_es(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    # Steam each word of the list
    words_stem = [stem_es(ww) for ww in words]
    for idx, w in enumerate(words_stem):
        if w in sentence_words: 
            bag[idx] = 1

    return bag