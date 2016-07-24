from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.

class PostList(ListView):
    template_name = 'semacomp2016/index.html'
    model = Post
