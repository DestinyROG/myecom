from django.contrib import admin
from NewApp.models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'image',
    ]    


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=[
        'category',
        'name',
    ]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'name',
        'quantity'
    ]