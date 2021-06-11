from django.urls import path
from lesson_11 import views

urlpatterns = [
    path('',views.lesson_1_1, name='lesson_1_1'),
]