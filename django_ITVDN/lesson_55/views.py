from django.shortcuts import render
from django.http import HttpResponse

from lesson_55.models import Category, Goods, ClientInternet


def index(request):
    return HttpResponse(request)

def create_goods(request):
    goods = Goods()
    goods.description = "Ключевые преимущества совместимых картриджа Vinga:" \
                        "Изготовлены исключительно в новых корпусах. " \
                        "В них отсутствуют следы использования или просыпания тонера в " \
                        "отличие от восстановленных оригинальных. " \
                        "Готовы к работе «из коробки» и не нуждаются в установке специальных чипов " \
                        "или других манипуляциях. " \
                        "Все комплектующие выполнены из качественных материалов, " \
                        "что гарантирует долговечность использования." \
                        "Стоимость в несколько раз ниже, чем у оригиналов, поэтому покупка не ударит по карману."
    goods.url_wiki = "https://www.itbox.ua/ru/product/Kartridjh_Vinga_Samsung_MLT-D111S_SL-M2020_2020W_2070_V-L-SMLT-D111A-p291215/"
    goods.name = 'Картридж Vinga Samsung MLT-D111S, SL-M2020/2020W/2070'
    goods.price = 400
    goods.save()
    return HttpResponse('Created!')


def create_category(request):
    category = Category()
    category.name = "Картриджи"
    return HttpResponse("Created!")


def create_client(request):

    return HttpResponse("Created!")


def get_goods(request):
    return HttpResponse('!!!')
