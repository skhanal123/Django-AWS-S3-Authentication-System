from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name = 'core_home_page'),
    
]