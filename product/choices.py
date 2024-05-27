from django.db import models


class CategotyType(models.IntegerChoices):
    NON_TYPE = 0, 'Non_type'
    CLOTHES = 1, 'Clothes'
    FOOD = 2, 'Food'
