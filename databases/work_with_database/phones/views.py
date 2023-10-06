from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    context = {
        'phones': Phone.objects.all()
        }

    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.filter(slug=slug)[0]
    }

    return render(request, template, context)
