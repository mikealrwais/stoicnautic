from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry_list),
    path('<slug:slug>', views.entry_detail),
]
