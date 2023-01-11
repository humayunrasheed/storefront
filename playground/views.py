from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def say_hello(request): 
    try:
        product = Product.objects.get(pk=1) 
    except ObjectDoesNotExist:
        pass
    #or
    product = Product.objects.filter(pk=0).first() #if the first element is empty the product = None
    exists = Product.objects.filter(pk=0).exists()
    return render(request, 'hello.html', {'name': 'Mosh'})
