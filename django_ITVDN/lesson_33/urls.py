from django.urls import path
from lesson_33 import views


urlpatterns = [
    path('index/', views.index),
    path('start/', views.start),
    path('start/lei/', views.lei),
    path('start/luke/', views.luke),
    path('start/khan/', views.khan),
]
