from django.urls import path
from itvdn import views


urlpatterns = [
    path('category/', views.categories, name='categories'),
    path('product/', views.products, name='products'),
    path('list/', views.base_list, name='base_list')
]
