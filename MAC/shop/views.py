from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


def index(request):
    fetchedProducts = Product.objects.all()
    n = len(fetchedProducts)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {
        "noOfSlides": nSlides,
        'range': range(1,nSlides),
        "products": fetchedProducts
    }
    return render(request, 'shop/index.html', params)


def search(request):
    return HttpResponse("At Search")


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("At Contact")


def productView(request):
    return HttpResponse("At Product View")


def tracker(request):
    return HttpResponse("At Tracker")


def checkout(request):
    return HttpResponse("At Checkout")
