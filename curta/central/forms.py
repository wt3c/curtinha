from django import forms
from .models import Curtinha

class CurtinhaForm(forms.Form):
    url_original = forms.URLField()
    url_curta = forms.URLField(max_length=50)
