from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    lets_do_it = [{'priority': 100, 'task': 'Составить список дел'},
                  {'priority': 150, 'task': 'Изучать Django'},
                  {'priority': 1, 'task': 'Подумать о смысле жизни'}]
    response = JsonResponse(lets_do_it, safe=False)
    return response


def start(request):
    return HttpResponse(request, 'start.html')


def luke(request):
    return HttpResponse("Страница Люка: "
                        "Люк Скайуокер — один из главных персонажей вселенной «Звёздных войн»,"
                        " джедай, сын сенатора с Набу Падме Амидалы Наберри и рыцаря-джедая Энакина Скайуокера")


def lei(request):
    return HttpResponse("Страница Леи: "
                        "Лея Органа — дочь рыцаря-джедая Энакина Скайуокера и сенатора Падме Амидалы Наберри.")


def khan(request):
    return HttpResponse("Страница Хана: "
                        "Хан. Соло — пилот космического корабля «Тысячелетний сокол»,"
                        " его бортмехаником и вторым пилотом является вуки по имени Чубакка.")
