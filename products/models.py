from django.db import models


# Create your models here.


class ProductCategories(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="Категория")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товаров"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=256, verbose_name="Наименование")
    image = models.ImageField(upload_to="products_images", blank=True, verbose_name="Фото")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
