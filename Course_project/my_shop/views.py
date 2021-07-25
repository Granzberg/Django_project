from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Choice
from .forms import RegistrationUser, SearchForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.urls import reverse


class Products(TemplateView):
    extra_context = {'form': SearchForm}
    template_name = 'product_list.html'
    context_object_name = 'categories', 'product'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(Products, self).get_context_data(**kwargs)
        context.update({
            'categories': Category.objects.order_by('name'),
            'products': Product.objects.order_by('name'),
        })
        return context

    def post(self, request):
        print(request.POST)


class HomePageView(TemplateView):
    template_name = 'base.html'


class SearchResultsView(ListView):
    model = Product
    template_name = 'search_page.html'

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__icontains=query)
        )
        return object_list


class ProductsView(DetailView):
    model = Product
    template_name = 'my_shop/product_detail.html'
    context_object_name = 'product'


def detail_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    print('sdsadad', pk)
    return render(request, 'my_shop/product_detail.html', context={'product': product})
