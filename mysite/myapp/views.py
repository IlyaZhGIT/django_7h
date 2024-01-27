from importlib.resources import contents
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from .models import Product


# Create your views here.
def products(request):
    page_object = items = Product.objects.all()

    item_name = request.GET.get("search")
    if item_name != "" and item_name is not None:
        page_object = items.filter(name__icontains=item_name)

    paginator = Paginator(page_object, 3)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    context = {"page_obj": page_object}
    return render(request, "myapp/products.html", context)


# class ProductListView(ListView):
#     model = Product
#     template_name = "myapp/products.html"
#     context_object_name = "items"
#     paginate_by = 3


# def product_id(request, my_id):
#     item = Product.objects.get(id=my_id)
#     context = {"item": item}
#     return render(request, "myapp/detail.html", context=context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "myapp/detail.html"
    context_object_name = "item"


@login_required
def additem(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES["upload"]
        seller = request.user
        item = Product(
            name=name, price=price, description=description, image=image, seller=seller
        )
        item.save()
    return render(request, "myapp/additem.html")


@login_required
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


# @login_required
# def deleteitem(request, my_id):
#     item = Product.objects.get(id=my_id)
#     if request.method == "POST":
#         item.delete()
#         return redirect("/myapp/products")
#     context = {"item": item}
#     return render(request, "myapp/deleteitem.html", context=context)


class DeleteItem(DeleteView):
    model = Product
    success_url = reverse_lazy("myapp:products")
