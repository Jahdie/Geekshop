from django.urls import path
from .views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='home_page'),
    path('<int:category_id>/', products, name='product'),
    path('page/<int:page>/', products, name='page'),
]
