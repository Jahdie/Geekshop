from django.shortcuts import render
import datetime
from products.models import ProductCategories, Products
# import json
# import os


def index(request):
    context = {
        "date_time": datetime.datetime.now(),
        "title": "GeekShop",
        "username": "Иван Иванов",
        "is_promotion": 1,
        "promotion_text": "Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям."
    }
    return render(request, "index.html", context)


def products(request):
    context = {"title": "GeekShop - Товары",
               "products": Products.objects.all(),
               "categories": ProductCategories.objects.all()}
    return render(request, "products.html", context)



