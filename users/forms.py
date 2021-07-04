from django.contrib.auth.forms import AuthenticationForm
from users.models import Users
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = Users
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'image')
