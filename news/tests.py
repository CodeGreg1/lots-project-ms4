from django.test import TestCase
from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
setup()


from .models import Post

class PostTestCase(TestCase):
    def test_queryset_exists(self):
        qs = Post.objects.all()
        self.assertTrue(qs.exists())