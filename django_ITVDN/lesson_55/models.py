from django.db import models
from datetime import datetime


class Сartridge(models.Model):
    count = models.IntegerField(default=0, blank=True, null=True)
    description = models.TextField(null=True)
    delivered_at = models.DateField(auto_now_add=True, blank=True, null=True)
    name = models.TextField(unique=True, null=True)


class Client(models.Model):
    name = models.CharField(max_length=64)
    user_uuid = models.UUIDField(editable=False, null=True)

    def __str__(self):
        return self.name


class Basket(models.Model):
    shop = models.Manager()
    help_text = 'Use with care and discretion.'
    count = models.IntegerField(default=1, null=True)
    cartridge = models.ManyToManyField(Сartridge)
