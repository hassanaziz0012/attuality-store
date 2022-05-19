from django.contrib import admin
from main.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discounted_price', 'image', 'order')
    search_fields = ('name',)
