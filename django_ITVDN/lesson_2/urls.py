from django.urls import path
from lesson_2 import views

urlpatterns = [
    path('index/', views.index, name='index-view'),
    path('bio/<username>/', views.bio, name='bio'),
    path('article/<int:year>/', views.year_archive),
    path('home/', views.home, name='home-view'),
    path('book/<title>/', views.book, name='book'),
]
