from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def homepage(request):
    return render(request, 'central/index.html')

# TESTE
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
    return homepage(request)
