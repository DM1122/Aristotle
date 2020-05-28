from django.urls import path
from . import views

urlpatterns = [
    path('', views.browser, name='library-browser')
]