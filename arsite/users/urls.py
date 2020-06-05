"""url paths for users app."""

# django
from django.urls import path

from . import views

urlpatterns = [
    path("", views.registration, name="users-registration"),
]
