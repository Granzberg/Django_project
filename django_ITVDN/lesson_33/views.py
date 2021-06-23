from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    lets_do_it = [{'priority': 100, 'task': 'Составить список дел'},
                  {'priority': 150, 'task': 'Изучать Django'},
                  {'priority': 1, 'task': 'Подумать о смысле жизни'}]
    response = JsonResponse(lets_do_it, safe=False)
    return HttpResponse(request, 'index.html', content=response)
