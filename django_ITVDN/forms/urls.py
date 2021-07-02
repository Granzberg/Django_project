from django.urls import path
from forms import views


urlpatterns = [
    path('', views.form),
    path('human/', views.index_human),

]