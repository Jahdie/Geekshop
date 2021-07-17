from django.shortcuts import render, HttpResponseRedirect
from users.models import Users
from products.models import Products, ProductCategories
from admins.forms import *
from django.urls import reverse


def index(request):
    context = {'title': 'Админ - панель'}
    return render(request, 'admins/index.html', context)


def admin_users_read(request):
    context = {'title': 'Админ - панель - Пользователи', 'users': Users.objects.all()}
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        register_form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('admins:admins_users_read'))
    else:
        register_form = UserAdminRegistrationForm()

    context = {'title': 'Админ-панель - Создание нового пользователя',
               'form': register_form,
               }
    return render(request, 'admins/admin-users-create.html', context)


def admin_users_update(request, pk):
    selected_user = Users.objects.get(id=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admins_users_read'))
    else:
        form = UserAdminProfileForm(instance=selected_user)

    context = {
        'title': 'Админ-панель - Редактирование пользователя',
        'form': form,
        'selected_user': selected_user
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


def admin_users_delete(request, pk):
    user = Users.objects.get(id=pk)
    user.delete()
    return HttpResponseRedirect(reverse('admins:admins_users_read'))


def admin_products_read(request):
    context = {'title': 'Админ - панель - Продукты', 'products': Products.objects.all()}
    return render(request, 'products/admin-products-read.html', context)


def admin_products_update(request, pk):
    selected_product = Products.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductAdminCreateForm(instance=selected_product, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admins_products_read'))
    else:
        form = ProductAdminCreateForm(instance=selected_product)
    context = {
        'title': 'Админ-панель - Редактирование продукта',
        'form': form,
        'selected_product': selected_product
    }
    return render(request, 'products/admin-products-update-delete.html', context)


def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminCreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admins_products_read'))
    else:
        form = ProductAdminCreateForm()

    context = {'title': 'Админ-панель - Создание нового пользователя',
               'form': form,
               }
    return render(request, 'products/admin-products-create.html', context)


def admin_products_delete(request, pk):
    product = Products.objects.get(id=pk)
    product.delete()
    return HttpResponseRedirect(reverse('admins:admins_products_read'))


def admin_categories_read(request):
    context = {'title': 'Админ - панель - Категории', 'categories': ProductCategories.objects.all()}
    return render(request, 'categories/admin-categories-read.html', context)


def admin_categories_update(request, pk):
    selected_category = ProductCategories.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoriesAdminCreateForm(instance=selected_category, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admins_categories_read'))
    else:
        form = ProductAdminCreateForm(instance=selected_category)
    context = {
        'title': 'Админ-панель - Редактирование категории',
        'form': form,
        'selected_category': selected_category
    }
    return render(request, 'categories/admin-categories-update-delete.html', context)


def admin_categories_create(request):
    if request.method == 'POST':
        form = CategoriesAdminCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admins_categories_read'))
    else:
        form = CategoriesAdminCreateForm()

    context = {'title': 'Админ-панель - Создание новой категории',
               'form': form,
               }
    return render(request, 'categories/admin-categories-create.html', context)


def admin_categories_delete(request, pk):
    category = ProductCategories.objects.get(id=pk)
    category.delete()
    return HttpResponseRedirect(reverse('admins:admins_categories_read'))
