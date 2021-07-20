from django.shortcuts import render
import datetime
from products.models import ProductCategories, Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {
        "date_time": datetime.datetime.now(),
        "title": "GeekShop",
        "is_promotion": 1,
        "promotion_text": "Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям."
    }
    return render(request, "index.html", context)


def products(request, category_id=None, page=1):
    context = {'title': 'GeekShop - Товары', 'categories': ProductCategories.objects.all()}
    if category_id:
        _products = Products.objects.filter(category_id=category_id)
    else:
        _products = Products.objects.all()
    paginator = Paginator(_products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, "products.html", context)



