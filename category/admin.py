from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'id']
    prepopulated_fields = {'slug': ('category',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'description', 'price']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)