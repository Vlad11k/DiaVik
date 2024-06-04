from django.contrib.admin.models import LogEntry
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models

from DiaVik import settings
from sales.models import Client

from django.core.mail import send_mail

user_password = None


class User(AbstractUser):
    address = models.CharField(max_length=255, default='', verbose_name="Адрес доставки")

    def set_password(self, raw_password):
        global user_password
        user_password = raw_password
        self.password = make_password(raw_password)
        self._password = raw_password

    def save(self, *args, **kwargs):
        if not Client.objects.filter(
                email=self.email).exists() and self.first_name and self.username and self.last_name:
            first_name, last_name, email = self.first_name, self.last_name, self.email
            Client.objects.create(first_name=first_name, last_name=last_name, email=email)

            subject = 'Скидочная программа'
            message = f'''
                        Добрый день! Вы были добавлены в скидочную программу DiaVik.by
                        Ваш логин: {self.username}
                        Ваш пароль: {user_password}
                        '''
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

        super().save(*args, **kwargs)
