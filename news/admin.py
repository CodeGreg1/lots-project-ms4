from django import forms
from django.contrib import admin
from .models import Post
from ckeditor.widgets import CKEditorWidget


class PostAdmin(admin.ModelAdmin):
    content = forms.CharField(widget=CKEditorWidget())
    list_display = ('title', 'slug', 'status', 'created_on',)
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
