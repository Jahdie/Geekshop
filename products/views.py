from django.shortcuts import render
import datetime
from products.models import ProductCategories, Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from common.views import CommonContextMixin


class IndexView(CommonContextMixin, TemplateView):
    template_name = 'index.html'
    title = 'GeekShop'


# def index(request):
#     context = {
#         "date_time": datetime.datetime.now(),
#         "title": "GeekShop",
#         "is_promotion": 1,
#         "promotion_text": "Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям."
#     }
#     return render(request, "index.html", context)


class ProductsListView(CommonContextMixin, ListView):
    model = Products
    template_name = 'products.html'
    paginate_by = 3
    title = 'GeekShop - Каталог'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategories.objects.all()
        return context


# def products(request, category_id=None, page=1):
#     context = {'title': 'GeekShop - Товары', 'categories': ProductCategories.objects.all()}
#     if category_id:
#         _products = Products.objects.filter(category_id=category_id)
#     else:
#         _products = Products.objects.all()
#     paginator = Paginator(_products, 3)
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#     context['products'] = products_paginator
#     return render(request, "products.html", context)
