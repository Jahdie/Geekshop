from django.contrib import admin
from products.models import ProductCategories, Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "description", "price", "quantity", "category")


class ProductCategoriesAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "description")


admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductCategories, ProductCategoriesAdmin)
