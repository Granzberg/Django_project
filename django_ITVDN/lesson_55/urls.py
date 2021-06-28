from django.urls import path
from lesson_55 import views


urlpatterns = [
    path('', views.index)
]
