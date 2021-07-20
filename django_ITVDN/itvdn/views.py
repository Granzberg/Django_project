from django.shortcuts import render
from .models import Product, Category
from .forms import RegistrationUser, SearchForm
from django.views.generic import TemplateView


class ProductList(TemplateView):
    extra_context = {'form':SearchForm}
    template_name = 'product_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all
        return context

    def post(self, request):
        print(request.POST)


def products(request):
    data = Product.objects.all()
    context = {'products': data}
    return render(request, 'product_list.html', context=context)


def categories(request):
    data = Category.objects.all()
    context = {'categories': data}
    for row in data:
        print(row)
    return render(request, 'product_list.html', context=context)


def base_list(request):
    data1 = Category.objects.all()
    data2 = Product.objects.all()
    context = {'categories': data1, 'products': data2}
    return render(request, 'product_list.html', context=context)


def product_search(request):
    context = {
        'form': SearchForm
    }
    return render(request, 'search_page.html', context=context)


def search_result(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        form.save()
    return render(request, 'search_page.html')



