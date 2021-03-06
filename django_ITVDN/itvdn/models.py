from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    objects = None
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):

    objects = None
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name
