from django.shortcuts import render
import datetime
from products.models import ProductCategories, Products


def index(request):
    context = {
        "date_time": datetime.datetime.now(),
        "title": "GeekShop",
        "is_promotion": 1,
        "promotion_text": "Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям."
    }
    return render(request, "index.html", context)


def products(request, category_id=None):
    context = {'title': 'GeekShop - Товары', 'categories': ProductCategories.objects.all()}
    if category_id:
        _products = Products.objects.filter(category_id=category_id)
    else:
        _products = Products.objects.all()
    context['products'] = _products
    return render(request, "products.html", context)



