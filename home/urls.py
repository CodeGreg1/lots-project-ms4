from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about_us.html', views.about_us, name='about_us'),
    path('links.html', views.links, name='links'),
    path('membership.html', views.membership, name='membership'),
    path('publications.html', views.publications, name='publications'),
    path('sales.html', views.sales, name='sales'),
    path('news.html', views.news, name='news'),
]
