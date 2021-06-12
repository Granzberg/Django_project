from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')


def bio(request, username):
    print(username)
    return HttpResponse(f'{username}')


def special_case_2003(request):
    print(request)
    return HttpResponse('special_case_2003')


def year_archive(request, year):
    print(request)
    print(year)
    if year == 2003:
        return HttpResponse('special_case_2003')
    return HttpResponse(f'{year}')


def home(request):
    print(request)
    return HttpResponse(request)


def book(request, title):
    print(request)
    return HttpResponse(f'{title}')
