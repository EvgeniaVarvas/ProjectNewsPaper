from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class NewsList(ListView):
    model = Post
    ordering = '-created'
    template_name = 'news.html'
    context_object_name = 'news'