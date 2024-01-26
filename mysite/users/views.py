from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import NewUserForms

# Create your views here.


def register(request):
    if request.method == "POST":
        form = NewUserForms(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("myapp:products")
    form = NewUserForms()
    context = {"form": form}
    return render(request, "user/register.html", context=context)
