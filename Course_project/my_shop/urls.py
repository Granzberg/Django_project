from django.urls import path
from my_shop import views


urlpatterns = [
    path('', views.Products.as_view(), name='products'),

]