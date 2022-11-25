from django.contrib import admin
from django.urls import path
from maps import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('map/', views.map, name='map_page'),
]
