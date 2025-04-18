from django.urls import path, register_converter
from nobels import views, converters

register_converter(converters.FourDigitYearConverter, "year4")
urlpatterns = [
    path('', views.index, name='home'),
    path('cats/<slug:cat_slug>/', views.categories, name='cats'),
    path('archive/<year4:year>/', views.archive, name='archive'),

]