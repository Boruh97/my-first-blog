from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('katalog/', views.cat),
    path('cake/', views.cake),
    path('cake/de-scripts/', views.de_scripts),
    path('base/de-scripts/', views.base_de_scripts),
]