from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegisterForm
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
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        register_form = UserRegisterForm()

    context = {'title': 'Geekshop - регистация',
               'form': register_form,
               }

    return render(request, 'registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
