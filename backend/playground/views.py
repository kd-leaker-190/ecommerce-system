from django.shortcuts import render
from store.models import Product, Order

def say_hello(request):
    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set').order_by('-placed_at')[:5]

    return render(request, 'index.html', { 
        'name': 'Shakib', 
        'orders': list(queryset) 
    })
