from django.urls import path
from django.views import ProductsList


urlpatterns = [
    path('', ProductsList.as_view(), name='products'),

]