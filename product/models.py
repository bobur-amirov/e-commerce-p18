from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from .choices import CategotyType

from base.models import TimeStampModel

User = get_user_model()


class Category(TimeStampModel):
    name = models.CharField(max_length=100, unique=True)
    order = models.IntegerField(default=0)
    type = models.IntegerField(choices=CategotyType, default=CategotyType.NON_TYPE)

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

    # def save(self, *args, **kwargs):
    #     self.validate_detail()
    #     super().save(*args, **kwargs)

    def validate_detail(self):
        category_type = self.category.type
        if category_type == 1:
            required_keys = {'size', 'color'}
        else:
            required_keys = set()

        missing_keys = required_keys - self.detail.keys()
        if missing_keys:
            raise ValidationError(
                "Missing required keys for category type '%(category_type)s': %(missing_keys)s",
                params={'category_type': category_type, 'missing_keys': ', '.join(missing_keys)},
            )


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
