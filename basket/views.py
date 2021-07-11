from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from products.models import Products
from basket.models import Baskets
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse


@login_required()
def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Baskets.objects.filter(user=request.user, product=product)

    def add_product():
        if not baskets.exists():
            Baskets.objects.create(user=request.user, product=product, quantity=1)
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()

    if 'login' in request.META.get('HTTP_REFERER'):
        add_product()
        return HttpResponseRedirect(reverse('products:home_page'))
    else:
        add_product()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def basket_remove(request, product_id):
    basket = Baskets.objects.get(id=product_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def basket_edit(request, basket_id, quantity):
    if request.is_ajax():
        basket = Baskets.objects.get(id=basket_id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Baskets.objects.filter(user=request.user)
        context = {'baskets': baskets}
        result = render_to_string('basket.html', context)
        return JsonResponse({'result': result})
