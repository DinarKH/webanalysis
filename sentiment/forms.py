from django import forms


class InputForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))