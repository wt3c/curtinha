from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

from .models import Curtinha
from .forms import CurtinhaForm


class Homepage(View):

    def get_object(self, request, *args, **kwargs):

        if not self.request.user.is_anonymous:
            user = self.request.user
            curtas = Curtinha.objects.filter(owner__email=user.email).order_by('-pk')
        else:
            curtas = Curtinha.objects.filter(owner=None).order_by('-pk')

        return curtas

    def get(self, request, *args, **kwargs):

        curtas = self.get_object(self.request)
        return render(request, 'central/index.html', {'form': CurtinhaForm(), 'curta': curtas})

    def post(self, request, *args, **kwargs):

        form = CurtinhaForm(self.request.POST)

        if form.is_valid():
            if not self.request.user.is_anonymous:
                user = self.request.user.pk
            else:
                user = None

            url = request.get_raw_uri()
            prefixo_url = url + 'c/'

            form.save(self.request.POST, owner=user, prefixo_url=prefixo_url)

            return HttpResponseRedirect('/', {'form': CurtinhaForm()})
        else:
            print('DEU RUIM')
            print(form.errors)
            print()


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')
        else:
            return render(request, 'central/login.html', {'form': form})
    else:
        return render(request, 'central/login.html', {'form': AuthenticationForm()})


def logout(request):
    auth_logout(request)
    
    curtas = Curtinha.objects.filter(owner=None).order_by('-pk')
    return render(request, 'central/index.html', {'form': CurtinhaForm(), 'curta': curtas})


def redirect_url(request):
    url = request.get_raw_uri()
    curta = Curtinha.objects.get(url_curta=url)

    return HttpResponseRedirect(str(curta.url_original))
