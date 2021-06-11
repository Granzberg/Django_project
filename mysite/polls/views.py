from django.shortcuts import render, HttpResponse


def hello(request):
    print("Hi!")
    return HttpResponse('Hello, world!')
