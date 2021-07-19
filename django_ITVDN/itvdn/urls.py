from django.urls import path
from itvdn import views


urlpatterns = [
    path('category/', views.categories, name='categories'),
    path('product/', views.products, name='products'),
    path('list/', views.base_list, name='base_list'),
    path('search/', views.product_search, name='product_search'),
    path('result/', views.search_result, name='search_result'),
    path('login/',views.registration_user, name='registration_user'),
    path('form-save/', views.user_form_save, name='user_form_save'),
]
