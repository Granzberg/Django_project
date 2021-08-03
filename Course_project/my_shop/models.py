from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Product(models.Model):
    objects = None
    name = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    image = models.ImageField(upload_to='media/', verbose_name='image')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Choice(models.Model):
    DoesNotExist = None
    name = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    name = models.TextField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)

    class Meta:
        ordering = ['create_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class AccountModel(models.Model):
    username = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField()
    date_joined = models.DateTimeField()
    password = models.CharField()
    last_login = models.DateTimeField()
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)


class CustomUser(AbstractUser):
    def save(self, *args, **kwargs):
        data = super(CustomUser, self).save(*args, **kwargs)
        AccountModel.objects.create(
            user=self,
        )
        return data
