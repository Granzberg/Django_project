from django.urls import path
from my_shop import views


from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('product-list/', views.Products.as_view(), name='product-list'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('product_views/<int:pk>/', views.detail_product, name='product'),
    path('register/', views.RegistrationUser, name='register_user'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]

