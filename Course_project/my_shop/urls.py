from django.urls import path
from my_shop import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('product-list/', views.Products.as_view(), name='product-list'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('product_views/<int:pk>/', views.detail_product, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
