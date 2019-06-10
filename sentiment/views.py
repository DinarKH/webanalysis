from django.shortcuts import render, HttpResponse
from . import forms, parse, text_cleaner


def inputRequest(request):
    if request.method == 'POST':
        url = request.POST['search_query']
        # sentiment = parse.getsentiment(url)
        if(url==''):
            header = 'Ошибка адреса'
            text = []
            sentiment = 'Ошибка адреса'
        else:
            header, text, analysis_text, sentiment = parse.parse(url)
        return render(request, 'answ.html',
                      {
                          'form': forms.InputForm,
                          'text': text,
                          'header': header,
                          'sentiment': sentiment,
                      })

    return render(request, 'input.html',
                  {
                      'form': forms.InputForm,
                  })


