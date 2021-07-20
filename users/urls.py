from django.urls import path
from .views import UserLoginView, UserLogoutView, UserRegistrationView, UserProfileView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
]