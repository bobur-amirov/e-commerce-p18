from django.contrib import admin

from .models import Category, Product, Images, Comment

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Images)
admin.site.register(Comment)

