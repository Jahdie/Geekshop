from django.urls import path

from admins.views import index, admin_users_create, admin_users_read, admin_users_update_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users_read, name='admins_users_read'),
    path('users-create/', admin_users_create, name='admins_users_create'),
    path('users-update-delete/', admin_users_update_delete, name='admins_users_update_create'),
    ]
