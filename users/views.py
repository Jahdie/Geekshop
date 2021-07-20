from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.urls import reverse
from basket.models import Baskets


def login(request):
    login_form = UserLoginForm(data=request.POST)
    _next = request.GET['next'] if 'next' in request.GET.keys() else ''
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('index'))

    else:
        login_form = UserLoginForm()
    context = {'title': 'Geekshop - вход',
               'form': login_form,
               'next': _next
               }

    return render(request, 'login.html', context)


def registration(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(data=request.POST, files=request.FILES)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        register_form = UserRegisterForm()

    context = {'title': 'Geekshop - регистация',
               'form': register_form,
               }

    return render(request, 'registration.html', context)


@login_required()
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(instance=user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=user)

    context = {
        'title': 'GeekShop - личный кабинет',
        'form': form,
        'baskets': Baskets.objects.filter(user=user),
    }
    return render(request, 'profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
