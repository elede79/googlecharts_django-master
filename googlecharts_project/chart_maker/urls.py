from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home_line/', views.home_line, name='home_line'),
]