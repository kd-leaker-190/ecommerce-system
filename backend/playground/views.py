from django.shortcuts import render
from store.models import Product

def say_hello(request):
    queryset = Product.objects.filter(description__isnull=True)

    return render(request, 'index.html', { 
        'name': 'Shakib', 
        'products': list(queryset) 
    })
