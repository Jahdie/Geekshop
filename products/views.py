from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import datetime


# Create your views here.


def index(request):
    context = {
        'date_time': datetime.datetime.now(),
        'title': 'GeekShop',
        'username': 'Иван Иванов',
        'is_promotion': 0,
        'promotion_text': 'Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
    }
    return render(request, 'index.html', context)


def products(request):
    context = {
        'date_time': datetime.datetime.now(),
        'categories': ['Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'],
        'title': 'GeekShop - Товары',
        'products': [
            {'card_title': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
             'img': '/static/vendor/img/products/Adidas-hoodie.png',
             'card_text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни'},
            {'card_title': 'Синяя куртка The North Face', 'price': 23725,
             'img': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
             'card_text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'card_title': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390,
             'img': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
             'card_text': 'Материал с плюшевой текстурой. Удобный и мягкий'},
            {'card_title': 'Черный рюкзак Nike Heritage', 'price': 2340,
             'img': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
             'card_text': 'Плотная ткань. Легкий материал.'},
            {'card_title': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590,
             'img': '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
             'card_text': 'Гладкий кожаный верх. Натуральный материал.'},
            {'card_title': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890,
             'img': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
             'card_text': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},
        ],
    }
    return render(request, 'products.html', context)
