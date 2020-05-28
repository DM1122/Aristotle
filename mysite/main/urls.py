from django.urls import path
from . import views
from users import views as users_views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('about/', views.about, name='main-about'),
    path('browser/', views.browser, name='main-browser'),
    path('register/', users_views.registration, name='users-registration'),
]