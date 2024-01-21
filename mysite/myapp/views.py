from django.shortcuts import render
from django.http import HttpResponse

from .models import Product


# Create your views here.
def products(request):
    items = Product.objects.all()
    context = {"items": items}
    return render(request, "myapp/product.html", context)


def product_id(request, my_id):
    item = Product.objects.get(id=my_id)
    context = {"item": item}
    return render(request, "myapp/detail.html", context=context)
