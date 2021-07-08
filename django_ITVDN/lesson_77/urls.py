from django.urls import path
from lesson_77 import views

urlpatterns =[
    path('test-form/',views.my_form_accounts, name='my_form'),
    path('second-test/', views.my_second_form, name='second_form'),
    path('modelform/', views.my_modelform, name='modelform')
]