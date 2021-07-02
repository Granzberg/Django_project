from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=65, blank=True)
    surname = models.CharField(max_length=65, blank=True)
    age = models.IntegerField(blank=True)
    company = models.TextField(max_length=200, blank=True)
    salary = models.IntegerField(blank=True)

