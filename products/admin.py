from django.contrib import admin
from .models import Product, Category 

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin): 
    list_display = (
        'name',
        'friendly_name',
    ) 

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

