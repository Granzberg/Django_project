from django.shortcuts import render
from .models import Product, Category
from .forms import RegistrationUser, SearchForm
from django.views.generic import TemplateView


class ProductsList(TemplateView):
    extra_context = {'form': SearchForm}
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all
        return context

    def post(self, request):
        print(request.POST)


def product_search(request):
    context = {
        'form': SearchForm
    }
    return render(request, 'search_page.html', context=context)