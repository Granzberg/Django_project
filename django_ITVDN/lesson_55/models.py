from django.db import models
from datetime import datetime, timedelta
import uuid


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

# ******************** internet shop ******************************************
class Category(models.Model):
    name = models.CharField(max_length=50, default=False, null=True)
    description = models.TextField(max_length=200, default=False, null=True)

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=65, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    url_wiki = models.URLField(default='https://uk.wikipedia.org/', blank=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    available = models.BooleanField(default=False)
    count = models.IntegerField(default=0, blank=True)
    when_available = models.DateTimeField(default=datetime.now, blank=True, null=True)
    discount_available = models.DurationField(default=timedelta(days=7), blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    discount  = models.FloatField(default=1.0, blank=True, null=True)
    link = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class ClientInternet(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    user_uuid = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4(), null=False)
    email = models.EmailField(blank=True, null=True)
    activation_date = models.DateField(auto_now=False, blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')
    invoice = models.FileField(blank=True, null=True)
    many_link = models.ManyToManyField(Goods, verbose_name='You ordered these goods.', blank=True)

    def __str__(self):
        return self.first_name