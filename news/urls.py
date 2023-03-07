from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.view_news, name='news'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
