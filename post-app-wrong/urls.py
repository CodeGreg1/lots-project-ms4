
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_posts, name='posts'),
    path('<post_id>/', views.post_detail, name='post_detail'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
