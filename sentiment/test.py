from django.test import TestCase
from .parse import parse, getsentiment


class FooTest(TestCase):
    def testparse(self):
        url = 'https://www.sport-interfax.ru/661702'
        header, text, analysis_text, sentiment = parse(url)
        analysis_text = analysis_text[:6]
        self.assertEqual(analysis_text, 'Надаль')

    def testempty(self):
        url = ''
        header, text, analysis_text, sentiment = parse(url)
        self.assertEqual(header, 'Некорректный ввод')

    def testerror(self):
        url = 'ya.ru'
        header, text, analysis_text, sentiment = parse(url)
        self.assertEqual(header, 'Некорректный ввод')

    def testsentiment(self):
        url = 'https://www.sport-interfax.ru/661702'
        sentiment = getsentiment(url)
        self.assertEqual(sentiment, 0)
