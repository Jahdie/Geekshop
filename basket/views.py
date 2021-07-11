from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from products.models import Products
from basket.models import Baskets
from django.urls import reverse


@login_required()
def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Baskets.objects.filter(user=request.user, product=product)

    def add_product():
        if not baskets.exists():
            Baskets.objects.create(user=request.user, product=product, quantity=1)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    if 'login' in request.META.get('HTTP_REFERER'):
        add_product()
        return HttpResponseRedirect(reverse('products:home_page'))
    else:
        add_product()


@login_required()
def basket_remove(request, product_id):
    basket = Baskets.objects.get(id=product_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
