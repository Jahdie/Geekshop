from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    login_form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        login_form = UserLoginForm()
    context = {'title': 'Geekshop - вход',
               'form': login_form,
               }
    return render(request, 'login.html', context)


def registration(request):
    return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
