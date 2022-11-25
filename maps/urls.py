from django.contrib import admin
from django.urls import path
from maps import views

urlpatterns = [
    path('map/', views.map, name='map_page'),
]
