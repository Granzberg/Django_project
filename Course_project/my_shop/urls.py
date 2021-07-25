from django.urls import path
from my_shop import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('product-list/', views.Products.as_view(), name='product-list'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('product_views/<int:pk>/', views.detail_product, name='product'),
]