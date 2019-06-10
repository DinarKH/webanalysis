# coding=utf8
from collections import OrderedDict
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import chi2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle


col_number = 3

negative_tweets = pd.read_csv(
    'negative.csv', header=None, delimiter=';')[[col_number]]
positive_tweets = pd.read_csv(
    'positive.csv', header=None, delimiter=';')[[col_number]]
train_range = 1500
df1 = positive_tweets[:train_range]
df2 = negative_tweets[:train_range]
frames = [df1, df2]
df = pd.concat(frames)
df.iloc[:, 0] = df.iloc[:, 0].str.replace(r"[^а-яА-Я ]", " ")

y_train = [1] * train_range + [0] * train_range
df['Sentiment'] = y_train
df = df.sample(frac=1)


X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 0], df['Sentiment'], random_state=0)

count_vect = CountVectorizer(ngram_range=(1,2))
new_text = count_vect.fit_transform(X_train.values.astype('U'))
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(new_text)
# NB = MultinomialNB()
model = RandomForestClassifier(n_estimators=50, max_depth=20, random_state=0)
clf = model.fit(X_train_tfidf, y_train)


with open('model.pkl', 'wb') as fout:
  pickle.dump((count_vect,clf), fout)

y_res = []
for el in X_test:
    y_res.append(clf.predict(count_vect.transform([el]))[0])

print(accuracy_score(y_res, y_test))
