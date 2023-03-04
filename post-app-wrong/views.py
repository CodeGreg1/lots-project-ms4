from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


# Create your views here.
def all_posts(request):
    """ A view to show all products """

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, "post/news_page.html", context)


def post_detail(request, post_id):
    """ A view to show individual products """

    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, "post/post_detail.html", context)
