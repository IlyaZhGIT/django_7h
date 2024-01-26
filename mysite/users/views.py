from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


from .forms import NewUserForms

# Create your views here.


@csrf_protect
def register(request):
    if request.method == "POST":
        form = NewUserForms(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("myapp:products")
        messages.add_message(request, messages.ERROR, "NOT VALID!")
    form = NewUserForms()
    context = {"form": form}
    return render(request, "user/register.html", context=context)
