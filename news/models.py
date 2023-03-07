from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # noqa
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(config_name='default')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
