from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from users.models import Users
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.urls import reverse
from basket.models import Baskets
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from common.views import CommonContextMixin


class UserLoginView(CommonContextMixin, LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    title = 'GeekShop - Авторизация'


# def login(request):
#     login_form = UserLoginForm(data=request.POST)
#     _next = request.GET['next'] if 'next' in request.GET.keys() else ''
#     if request.method == 'POST' and login_form.is_valid():
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = auth.authenticate(username=username, password=password)
#         if user and user.is_active:
#             auth.login(request, user)
#             if 'next' in request.POST.keys():
#                 return HttpResponseRedirect(request.POST['next'])
#             else:
#                 return HttpResponseRedirect(reverse('index'))
#
#     else:
#         login_form = UserLoginForm()
#     context = {'title': 'Geekshop - вход',
#                'form': login_form,
#                'next': _next
#                }
#
#     return render(request, 'login.html', context)

class UserRegistrationView(CommonContextMixin, SuccessMessageMixin, CreateView):
    model = Users
    form_class = UserRegisterForm
    template_name = 'registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегестрировались!'
    title = 'GeekShop - Регистрация'


# def registration(request):
#     if request.method == 'POST':
#         register_form = UserRegisterForm(data=request.POST, files=request.FILES)
#
#         if register_form.is_valid():
#             register_form.save()
#             messages.success(request, 'Вы успешно зарегистрировались!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         register_form = UserRegisterForm()
#
#     context = {'title': 'Geekshop - регистация',
#                'form': register_form,
#                }
#
#     return render(request, 'registration.html', context)

class UserProfileView(CommonContextMixin, UpdateView):
    model = Users
    form_class = UserProfileForm
    template_name = 'profile.html'
    title = 'GeekShop - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['baskets'] = Baskets.objects.filter(user=self.object)
        return context


# @login_required()
# def profile(request):
#     user = request.user
#     if request.method == 'POST':
#         form = UserProfileForm(instance=user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = UserProfileForm(instance=user)
#
#     context = {
#         'title': 'GeekShop - личный кабинет',
#         'form': form,
#         'baskets': Baskets.objects.filter(user=user),
#     }
#     return render(request, 'profile.html', context)


class UserLogoutView(LogoutView):
    pass
