from django.urls import path
from lesson_55 import views


urlpatterns = [
    path('', views.index),
    path('goods/', views.create_goods),
    path('clients/', views.create_client),
    path('category/', views.create_category),
]
