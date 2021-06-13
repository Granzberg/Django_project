from django.urls import path
from lesson_33 import views


urlpatterns = [
    path('index/', views.index),
]
