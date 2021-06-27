from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import datetime
import json
import os


# Create your views here.


def index(request):
    context = {
        "date_time": datetime.datetime.now(),
        "title": "GeekShop",
        "username": "Иван Иванов",
        "is_promotion": 0,
        "promotion_text": "Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям."
    }
    return render(request, "index.html", context)


def products(request):
    path_to_project = os.path.dirname(os.path.realpath(__file__))
    path_to_json = path_to_project + "\\fixtures\\products.json"
    with open(path_to_json, encoding="utf-8") as file:
        context = json.load(file)
    return render(request, "products.html", context)
