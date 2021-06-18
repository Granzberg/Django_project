from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    lets_do_it = [{'priority': 100, 'task': 'Составить список дел'},
                  {'priority': 150, 'task': 'Изучать Django'},
                  {'priority': 1, 'task': 'Подумать о смысле жизни'}]
    for _ in lets_do_it:
        return HttpResponse(request, 'index.html')
