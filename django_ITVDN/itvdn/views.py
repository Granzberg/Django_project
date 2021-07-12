from django.shortcuts import render
from django.http import HttpResponse


def product(request):
    return HttpResponse(request, 'product_list.html')


def category(request):
    return HttpResponse(request, 'base.html')
