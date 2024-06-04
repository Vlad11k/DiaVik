# Generated by Django 5.0.6 on 2024-05-09 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=40, verbose_name='Email')),
                ('percent', models.IntegerField(default=0, verbose_name='Скидка')),
                ('total_sum', models.FloatField(default=0, verbose_name='Общая сумма')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=30, verbose_name='Название')),
                ('is_available', models.BooleanField(default=False, verbose_name='Наличие')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Расцветки',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Позиция')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('is_available', models.BooleanField(default=False, verbose_name='Наличие')),
            ],
            options={
                'verbose_name': 'Позиция',
                'verbose_name_plural': 'Позиции',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')),
                ('total_price', models.FloatField(verbose_name='Сумма заказа')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.client', verbose_name='Клиент')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.color', verbose_name='Цвет')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.product', verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'История покупок',
                'verbose_name_plural': 'История покупок',
            },
        ),
    ]
