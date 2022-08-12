from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil


def index(request):
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {
        'allProds': allProds,
    }
    return render(request, 'shop/index.html', params)


def search(request):
    return render(request, 'shop/search.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def productView(request, myId):
    product = Product.objects.filter(id=myId)
    print(product)
    return render(request, 'shop/prodview.html',{'product':product[0]})


def tracker(request):
    return render(request, 'shop/tracker.html')


def checkout(request):
    return render(request, 'shop/checkout.html')
