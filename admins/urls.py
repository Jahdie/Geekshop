from django.urls import path

from admins.views import *

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admins_users_read'),
    path('users-create/', UserCreateView.as_view(), name='admins_users_create'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admins_users_delete'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admins_users_update'),
    path('products/', admin_products_read, name='admins_products_read'),
    path('products-create/', admin_products_create, name='admins_products_create'),
    path('products-delete/<int:pk>/', admin_products_delete, name='admins_products_delete'),
    path('products-update/<int:pk>/', admin_products_update, name='admins_products_update'),
    path('categories/', admin_categories_read, name='admins_categories_read'),
    path('categories-create/', admin_categories_create, name='admins_categories_create'),
    path('categories-delete/<int:pk>/', admin_categories_delete, name='admins_categories_delete'),
    path('categories-update/<int:pk>/', admin_categories_update, name='admins_categories_update'),
]
