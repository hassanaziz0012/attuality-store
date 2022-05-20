from django.contrib import admin
from main.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'discounted_price', 'image', 'order')
    search_fields = ('name', 'brand')
    list_filter = ('brand', 'price', 'discounted_price')
