# Imports nécessaires
import pandas as pd
import numpy as np
import string

# Lecture et stockage de la base de données
tweet_df = pd.read_csv('../../delphes/data/final2_clean.csv', index_col=0)


# Remove the undesirable elements in the entire dataframe
def rmurl_df(df, column_name):
    '''
    This function removes all the URLs, the #hashtag and the @user of a column made of strings.
    Be careful to apply it BEFORE all the other preprocessing steps (if not it wont'
    be recognized as a URL)
    '''
    df = df.copy()
    df[column_name] = df[column_name].str.replace('http\S+|www.\S+|@\S+|#\S+', '', case=False)
    return df


# Lowercase the tweet's column
def lower_df(df, column_name):
    '''
    This function lowercases a column made of strings and return the dataframe.
    '''
    df = df.copy()
    df[column_name] = df[column_name].str.lower()
    return df


# Remove the numbers in the tweet's column
def rmnumbers_df(df, column_name):
    '''
    This function removes all the digits of a column made of strings.
    '''
    df = df.copy()
    def remove_numbers(text):
        return ''.join(word for word in text if not word.isdigit())
    df[column_name] = df[column_name].apply(remove_numbers)
    return df


# Remove the undesirable punctuations in the tweet's column
# Remove the undesirable punctuations in the tweet's column
def rmpunct_df(df, column_name):
    '''
    This function removes all the punctuations, all the "rt" and remove multiple spaces
    of a column made of strings.
    '''
    punct = string.punctuation
    df = df.copy()
    def replace_punct(text):
        for punctu in punct:
            text = text.replace(punctu, ' ')
            text = text.replace(' rt ','')
            text = " ".join(text.split())
        return text
    df[column_name] = df[column_name].apply(replace_punct)
    return df

# Remove the stopwords in the tweet's column
def rmstopwords_df(df, column_name):
    '''
    This function removes all the stopwords of a column made of strings.
    '''
    df = df.copy()
    stop_words = stopwords.words('english')
    def remove_stopwords(text):
        for word in stop_words:
            text = text.replace(f' {word} ', ' ')
        return text
    df[column_name] = df[column_name].apply(remove_stopwords)
    return df


# Remove the undesirable emojis in the entire dataframe
def rmemojis_df(df):
    '''
    This function removes all the emojis of a column made of strings.
    Be careful to translate in latin alphabet before applying this function :
    it also removes cyrillic alphabet.
    '''
    df = df.copy()
    df = df.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))
    return df

# Sentence embedding
def embed_sentence(word2vec, sentence):
    '''
    Embed one sentence.
    '''
    y = []
    for word in sentence:
        if word in word2vec.wv.vocab.keys():
           y.append(word2vec[word])
    return np.array(y)

#Sentence embedding
def embedding(word2vec, sentences):
    '''
    Embed  set of sentences.
    '''
    y = []
    for sentence in sentences:
        y.append(embed_sentence(word2vec, sentence))
    return y


# Cette fonction retourne automatiquement X_train, X_test, y_train, y_test de notre base de données twitter.
def get_train_test_objects(df, X, y):
    '''
    Les étapes que cette fonction réalise sont en commentaires. X est la/les colonnes qui sont nos inputs.
    y est la colonne de nos outputs.
    '''
    # Copie de la base de données pour éviter les problèmes d'assignation abusive.
    df = df.copy()
    # Récupération de tous les tweets et du nom du député qui les a posté. Création de la cible y.
    df = df[[X, y]]
    y1 = pd.get_dummies(df[y])
    # Transformation des tweets en suite de mots (strings) dans une liste.
    sentences = df[X]
    sentences_inter = []
    for sentence in sentences:
        sentences_inter.append(sentence.split())
    # Séparation des données d'entraînement et de test
    sentences_train, sentences_test, y_train, y_test = train_test_split(sentences_inter, y1, test_size = 0.3)
    # Vectorisation des phrases
    word2vec = Word2Vec(sentences=sentences_train)
    # Création des données d'entrée.
    X_train = embedding(word2vec,sentences_train)
    X_test = embedding(word2vec,sentences_test)
    X_train_pad = pad_sequences(X_train, padding='post',value=-1000, dtype='float32')
    X_test_pad = pad_sequences(X_test, padding='post',value=-1000, dtype='float32')
    # Création des données cibles.
    y_train = y_train.values
    y_test = y_test.values
    # Sorties de la fonction
    return X_train_pad, y_train, X_test_pad, y_test


# Modeling
def init_model():
    '''
    Initialise un modèle avec les couches spécifiées. Le compile pour effectuer une classification multiple.
    '''
    model = Sequential()
    model.add(layers.Masking(mask_value = -1000))
    model.add(layers.LSTM(15, activation='tanh'))
    model.add(layers.Dense(20, activation='relu'))
    model.add(layers.Dense(10, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
    return model
