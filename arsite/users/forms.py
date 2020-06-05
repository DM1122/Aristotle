"""User forms."""

# django
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    """Registration form."""

    email = forms.EmailField()

    class Meta:
        """Select fields to display in form."""

        model = User
        fields = ["username", "email", "password1", "password2"]
