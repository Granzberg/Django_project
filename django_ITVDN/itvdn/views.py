from django.shortcuts import render
from .models import Product, Category
from .forms import RegistrationUser, SearchForm


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
    return render(request, 'search_page.html')


def search_result(request):
    print(dir(request))
    return render(request, 'search_page.html')

def registration_user(request):
    context = {
        'form': RegistrationUser
    }
    return render(request, 'registration/login.html',context=context)

def user_form_save(request):
    form = RegistrationUser(request.GET)
    if form.is_valid():
        form.save()
    return render(request, 'registration/login.html')

def search_form(request):
    context = {
        'searchform':SearchForm
    }
    return render(request, 'search_page.html', context=context)
