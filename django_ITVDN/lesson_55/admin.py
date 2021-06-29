from django.contrib import admin
from . import models


admin.site.register(models.Сartridge)
admin.site.register(models.Basket)
admin.site.register(models.Client)

admin.site.register(models.ClientInternet)
admin.site.register(models.Goods)
admin.site.register(models.Category)
