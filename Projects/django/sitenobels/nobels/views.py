from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render
# Create your views here.

data_db = [
 {'id': 1, 'title': 'Анджелина Джоли', 'content':
'Биография Анджелины Джоли', 'is_published': True},
 {'id': 2, 'title': 'Марго Робби', 'content':
'Биография Марго Робби', 'is_published': False},
 {'id': 3, 'title': 'Джулия Робертс', 'content':
'Биография Джулия Робертс', 'is_published': True},
]

menu = [{'title': "О сайте", 'url_name': 'about'},
 {'title': "Добавить статью", 'url_name':
'add_page'},
 {'title': "Обратная связь", 'url_name':
'contact'},
 {'title': "Войти", 'url_name': 'login'}
]

def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db        
    }
    return render(request, 'nobels/index.html', data)    


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


def about(request):
    data = {'title': 'О сайте'}
    return render(request, 'nobels/about.html', data)


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")