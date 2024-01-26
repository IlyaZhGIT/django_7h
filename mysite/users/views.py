from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile


from .forms import NewUserForms

# Create your views here.


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
    return render(request, "users/register.html", context=context)


@login_required
def profile(request):
    if request.method == "POST":
        user = request.user
        contact_number = request.POST.get("number")
        image = request.FILES["upload"]
        user_profile = Profile(user=user, contact_number=contact_number, image=image)
        user_profile.save()
    return render(request, "users/profile.html")
