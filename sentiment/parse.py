from bs4 import BeautifulSoup
import urllib.request
from .models import dataset
import pickle
import os
from django.conf import settings

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(url):
    try:
        html = get_html(url).decode("cp1251")
        soup = BeautifulSoup(html, 'html.parser')
        header = soup.find_all("h1")
        header = header[0].get_text()
        analysis_text = header + " "
        art = soup.find_all('p')
        list_p = []
        start_index = art[0].get_text().find('-')
        new_text = art[0].get_text()[start_index + 2:]
        try:
            art[0].string.replace_with(new_text)
        except:
            print('error')
        for el in art:
            list_p.append(el.get_text())
            analysis_text = analysis_text + el.get_text() + " "
        result = use_model(analysis_text)
        # result = use_model(header)
        return header, list_p, analysis_text, result
    except Exception as e:
        print(e)
        # return 'Некорректный ввод', '', ''


def getsentiment(url):
    try:
        sentiment = dataset.objects.get(link=url).sentiment
    except:
        sentiment = 0
    return sentiment

def use_model(text):
    # my_path = os.path.join(settings.BASE_DIR, 'sentiment/model.pkl')
    with open(os.path.join(settings.BASE_DIR, 'sentiment\\model.pkl'),'rb') as fin:
        count_vect, clf = pickle.load(fin)
    pred_res = clf.predict_proba(count_vect.transform([text]))
    result = clf.predict(count_vect.transform([text]))
    print(pred_res)
    print(result)
    result = pred_res[0][1]//0.2+(-2)
    return result

