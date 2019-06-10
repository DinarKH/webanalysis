# coding=utf8

import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import chi2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt
import pickle

train_range = 4000
data_col_number = 3

negative_data = pd.read_csv(
    'negative.csv', header=None, delimiter=';')[[data_col_number]]
positive_data = pd.read_csv(
    'positive.csv',header=None, delimiter=';')[[data_col_number]]


df1 = positive_data[:train_range]
df2 = negative_data[:train_range]
frames = [df1, df2]
df = pd.concat(frames)
df.iloc[:,0]=df.iloc[:,0].str.replace(r"[^а-яА-Я ]", " ")
count_vect = CountVectorizer(ngram_range=(1, 2))
new_text = count_vect.fit_transform(df.iloc[:,0].values.astype('U'))
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(new_text)
# y_train = dataset['Sentiment']
y_train = [1]*train_range + [0] * train_range
# NB = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
NB = MultinomialNB()
clf = NB.fit(X_train_tfidf, y_train)

with open('model.pkl', 'wb') as fout:
  pickle.dump((count_vect,clf), fout)
  print('file complete')

#
# text = 'у меня сегодня прекрасный день'
# print(clf.predict_proba(count_vect.transform([text])))
# print(clf.predict(count_vect.transform([text])))
#
# text = 'взрыв куча жертв пострадавшие и погибшие'
# print(clf.predict_proba(count_vect.transform([text])))
# print(clf.predict(count_vect.transform([text])))

