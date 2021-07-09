from django.urls import path
from itvdn import views


urlpatterns =[
    path('category/', views.category,),
    path('product/', views.product,),
]
