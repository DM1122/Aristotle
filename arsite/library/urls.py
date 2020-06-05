"""Urls paths for library app."""
# django
from django.urls import path

from . import views

urlpatterns = [
    path("browser/", views.browser, name="library-browser"),
    path("theatre/", views.theatre, name="library-theatre"),
]
