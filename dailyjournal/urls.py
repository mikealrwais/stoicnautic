from django.contrib import admin
from django.urls import path
from . import views

app_name = 'dailyjournal'
urlpatterns = [
    path('', views.entry_list, name='list'),
    path('<slug:slug>', views.entry_detail, name='detail'),
]
