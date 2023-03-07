from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.views import generic
from .models import Post


def view_news(request):
    context = {
        'post': Post.objects.all(),
        'queryset': Post.objects.filter(status=1).order_by('-created_on'),
    }
    """ A view to return the News page """
    return render(request, "news/news.html", context)


class PostList(generic.ListView):
    template_name = 'news.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
