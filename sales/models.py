from django.db import models
from django.db.models import F


class Client(models.Model):
    first_name = models.CharField(max_length=25, verbose_name="Имя")
    last_name = models.CharField(max_length=25, verbose_name='Фамилия')
    email = models.EmailField(max_length=40, verbose_name="Email")
    percent = models.IntegerField(default=0, verbose_name="Скидка")
    total_sum = models.FloatField(default=0, verbose_name="Общая сумма")

    def __str__(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = "Клиенты"


class History(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name="Клиент")
    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING, verbose_name="Наименование")
    color = models.ForeignKey('Color', on_delete=models.DO_NOTHING, verbose_name="Цвет")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата покупки")
    total_price = models.FloatField(verbose_name="Сумма заказа")

    def __str__(self):
        full_name = self.client.first_name + ' ' + self.client.last_name
        return full_name

    class Meta:
        verbose_name = 'История покупок'
        verbose_name_plural = "История покупок"

    def save(self, *args, **kwargs):
        self.client.percent = self.get_discount(self.product.price)
        client = self.client
        buy_sum = self.product.price - self.product.price * (client.percent / 100)
        self.total_price = buy_sum
        client.total_sum = F('total_sum') + buy_sum
        client.save()
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.client.total_sum = F('total_sum') - self.total_price
        self.client.save()
        super().delete()

    def get_discount(self, buy_sum):
        client = self.client
        discount = 0
        if client.total_sum + buy_sum >= 900:
            discount = 15
        elif client.total_sum + buy_sum >= 500:
            discount = 7
        elif client.total_sum + buy_sum >= 300:
            discount = 5
        return discount


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name="Позиция")
    price = models.FloatField(verbose_name="Цена")
    is_available = models.BooleanField(default=False, verbose_name="Наличие")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = "Позиции"


class Color(models.Model):
    color_name = models.CharField(max_length=30, verbose_name="Название")
    is_available = models.BooleanField(default=False, verbose_name="Наличие")

    def __str__(self):
        return self.color_name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = "Расцветки"
