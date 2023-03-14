from django.test import TestCase
from django import setup
from .models import Post
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
setup()


class PostTestCase(TestCase):
    def test_queryset_exists(self):
        qs = Post.objects.all()
        self.assertTrue(qs.exists())
