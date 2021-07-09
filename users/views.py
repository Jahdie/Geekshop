from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from basket.models import Baskets
from django.db.models import Sum


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
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        register_form = UserRegisterForm()

    context = {'title': 'Geekshop - регистация',
               'form': register_form,
               }

    return render(request, 'registration.html', context)


def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(instance=user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=user)

    total_price = 0
    total_quantity = 0
    prices_and_quantity = Baskets.objects.filter(user=user).values('product__price', 'quantity')
    for item in prices_and_quantity:
        values = list(item.values())
        total_price += (values[0] * values[1])
        total_quantity += values[1]
        
    context = {
        'title': 'GeekShop - личный кабинет',
        'form': form,
        'baskets': Baskets.objects.filter(user=user),
        'total_price': total_price,
        'total_quantity': total_quantity,
    }
    return render(request, 'profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
