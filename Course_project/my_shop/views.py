from django.shortcuts import render
from .models import Product, Category
from .forms import RegistrationUser, SearchForm
from django.views.generic import TemplateView


class Products(TemplateView):
    extra_context = {'form': SearchForm}
    template_name = 'product_list.html'
    context_object_name = 'categories'
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





def product_search(request):
    context = {
        'form': SearchForm
    }
    return render(request, 'search_page.html', context=context)