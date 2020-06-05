"""Views for users app."""

# django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserRegisterForm

# from django.contrib.auth.forms import UserCreationForm


def registration(request):
    """Register form logic."""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("main-home")
    else:
        form = UserRegisterForm()

    return render(request, "users/registration.html", {"form": form})


@login_required
def profile(request):
    """Return profile view if user is logged in."""
    return render(request, "users/profile.html")
