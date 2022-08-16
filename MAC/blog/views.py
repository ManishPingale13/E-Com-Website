from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost


def index(request):
    blogs = Blogpost.objects.all()
    print(blogs)
    return render(request, 'blog/index.html', {'blogs': blogs})


def blogpost(request, id):
    post = Blogpost.objects.filter(postId=id)[0]
    return render(request, 'blog/blogpost.html', {'post': post})
