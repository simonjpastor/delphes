import pandas as pd
import pytz
from flask import Flask
from flask import request
from flask_cors import CORS
from termcolor import colored
from Trainer import embed_sentence, embedding
from gensim.models import Word2Vec

app = Flask(__name__)
CORS(app)

PATH_TO_MODEL = "delphes/data/model_deputies"
DATA_REF_PATH = "raw_data/cleaned_tweet_df"
MODEL_PATH = {"country":"delphes/data/model_country"}
WORD2VEC_PATH = {"country":"delphes/data/word2vec_country"}

text = ['i believe that cats are better than platypus']
feature = 'country'

model = keras.models.load_model(MODEL_PATH[feature])
word2vec = Word2Vec.load(WORD2VEC_PATH[feature])

def format_input(text, word2vec):
    sentences_inter = []
    for sentence in text:
        sentences_inter.append(sentence.split())
    X_train = embedding(word2vec,sentences_inter)
    formated_input = pad_sequences(X_train, padding='post',value=-1000, dtype='float32')
    return formated_input


pipeline_def = {'pipeline': model}




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
own("""
    ## **MODELS**
""")
