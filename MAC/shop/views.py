from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'shop/index.html')

def search(request):
    return HttpResponse("At Search")

def about(request):
    return HttpResponse("At About")

def contact(request):
    return HttpResponse("At Contact")

def productView(request):
    return HttpResponse("At Product View")

def tracker(request):
    return HttpResponse("At Tracker")

def checkout(request):
    return HttpResponse("At Checkout")