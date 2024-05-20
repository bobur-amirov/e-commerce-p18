from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from base.models import TimeStampModel

User = get_user_model()


class Category(TimeStampModel):
    name = models.CharField(max_length=100, unique=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Product(TimeStampModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()
    detail = models.JSONField(default=dict)

    def __str__(self):
        return self.title


class Images(TimeStampModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.product.title


class Comment(TimeStampModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=300)
    star = models.IntegerField(default=0,
                               validators=[MaxValueValidator(5), MinValueValidator(0)])

    def __str__(self):
        return self.product.title
