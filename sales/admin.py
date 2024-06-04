from django.contrib import admin
from django.db import transaction

from .models import *


class HistoryAdmin(admin.ModelAdmin):
    fields = ['client', 'product', 'color']
    list_display = ['client', 'product', 'color', 'total_price']
    ordering = ['-time_create', 'client']
    list_filter = ['client', 'product', 'color']
    
    def delete_queryset(self, request, queryset):
        with transaction.atomic():
            for obj in queryset:
                obj.delete()


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_available']
    list_editable = ['is_available']
    ordering = ['-is_available','name']


class ColorAdmin(admin.ModelAdmin):
    list_display = ['color_name', 'is_available']
    list_editable = ['is_available']
    ordering = ['-is_available', 'color_name']


admin.site.register(Client)
admin.site.register(History, HistoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Color, ColorAdmin)
