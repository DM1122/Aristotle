from django.urls import path
from . import views
#from users import views as users_views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('about/', views.about, name='main-about'),
    path('tools/', views.tools, name='main-tools'),
    path('vision/', views.vision, name='main-vision'),    

    # path('register/', users_views.registration, name='users-registration'),
]