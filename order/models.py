from django.db import models
from django.contrib.auth import get_user_model

from base.models import TimeStampModel
from product.models import Product

User = get_user_model()


class OrderItem(TimeStampModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    ordered = models.BooleanField(default=False)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name='orderitem')

    def __str__(self):
        return self.product.title

    def set_total_price(self):
        self.total_price = self.product.price * self.quantity
        self.save()
        return


class Order(TimeStampModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.username

    def set_total_price(self):
        total = 0
        for price in self.orderitem.objects.all():
            total += price.total_price
        self.total_price = total
        self.save()
        return
