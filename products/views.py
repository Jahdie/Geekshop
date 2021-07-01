from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import datetime
from products.models import ProductCategories, Products
import json
import os


# Create your views here.


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
    model_categories_content = ProductCategories.objects.all()
    model_products_content = Products.objects.all()
    context = {"title": "GeekShop - Товары",
               "products": model_products_content,
               "categories": model_categories_content}
    return render(request, "products.html", context)



