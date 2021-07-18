from django.urls import path
from itvdn import views


urlpatterns = [
    path('category/', views.categories, name='categories'),
    path('product/', views.products, name='products'),
    path('list/', views.base_list, name='base_list'),
    path('search/', views.product_search, name='product_search'),
    path('result/', views.search_result, name='search_result'),
]
