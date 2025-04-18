from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.


def index(request):
    return HttpResponse("Страница приложения nobels.")


def categories(request, cat_slug):
    if request.GET:
        print(request.GET)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p >slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        return redirect('home', permanent=True)
    elif year < 1901:
        url_redirect = reverse('cats', args=('music', ))
        return redirect(url_redirect)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
