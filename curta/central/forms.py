from django import forms
from django.contrib.auth.models import User
from random import choice
from string import ascii_letters, digits

from .models import Curtinha


class CurtinhaForm(forms.Form):
    url_original = forms.URLField(widget=forms.TextInput(attrs={'class': "form-control"}))
    url_curta = forms.URLField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': "float-right"}))

    def save(self, request, owner, prefixo_url):

        try:
            owner = User.objects.get(pk=owner)
        except User.DoesNotExist:
            owner = None

        alpha = ascii_letters + digits

        # 127.0.0.1/c/45s45i
        # "".join([chr(choice(range(48, 122))) for x in range(6)])

        prefixo = prefixo_url
        sufixo = "".join([choice(alpha) for x in range(6)])
        url_curta = str(prefixo + sufixo)

        Curtinha.objects.create(
            owner=owner,
            url_original=request['url_original'],
            url_curta=url_curta
        )
