from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Category, Product, Images, Comment, Country

# admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Images)
admin.site.register(Comment)


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['pk']


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name', 'order', 'type')
