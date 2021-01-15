from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.

def Blog(request):
    post  = Post.objects.all
    return render(request, 'blog.html', {'post': post }) 


class PostListView(ListView):
    model = Post
