from django.shortcuts import render
from django.views.generic import ListView
from django.utils import timezone

from .models import *
# Create your views here.

def home(request):
    sessions = Session.objects.all().order_by('published_date')
    sponsors = Sponsor.objects.all().order_by('-sponsor_level')
    return render(request, 'semacomp2016/home.html', {'sponsors': sponsors, 'sessions': sessions})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'semacomp2016/post_detail.html', {'post': post})
