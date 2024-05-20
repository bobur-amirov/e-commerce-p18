from django.db import models


class UserType(models.IntegerChoices):
    ADMIN = 0, 'Admin'
    CUSTOMER = 1, 'Customer'
