from django.urls import path
from .views import ProductsListView

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='home_page'),
    path('<int:category_id>/', ProductsListView.as_view(), name='product'),
    path('page/<int:page>/', ProductsListView.as_view(), name='page'),
]
