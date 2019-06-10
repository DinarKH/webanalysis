import pickle

with open('model.pkl', 'rb') as fin:
  count_vect,clf = pickle.load(fin)

text = 'у меня сегодня прекрасный день'
print(clf.predict_proba(count_vect.transform([text])))
print(clf.predict(count_vect.transform([text])))

text = 'взрыв куча жертв пострадавшие и погибшие'
print(clf.predict_proba(count_vect.transform([text])))
print(clf.predict(count_vect.transform([text])))