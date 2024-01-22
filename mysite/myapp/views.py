from importlib.resources import contents
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Product


# Create your views here.
def products(request):
    items = Product.objects.all()
    context = {"items": items}
    return render(request, "myapp/products.html", context)


def product_id(request, my_id):
    item = Product.objects.get(id=my_id)
    context = {"item": item}
    return render(request, "myapp/detail.html", context=context)


def additem(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES["upload"]
        item = Product(name=name, price=price, description=description, image=image)
        item.save()
    return render(request, "myapp/additem.html")


def updateitem(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.description = request.POST.get("description")
        item.image = request.FILES.get("upload", item.image)
        item.save()
        return redirect("/myapp/products")
    context = {"item": item}
    return render(request, "myapp/updateitem.html", context=context)


def deleteitem(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == "POST":
        item.delete()
        return redirect("/myapp/products")
    context = {"item": item}
    return render(request, "myapp/deleteitem.html", context=context)
