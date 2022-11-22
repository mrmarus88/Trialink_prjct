"""Trialink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('Trialink/', include('Trialink.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from main import views

table_patterns  = [
    path("", views.tables_main),
    path("servers", views.servers),
    path("terminals", views.terminals),
    path("bts", views.bts),
]

main_page_patterns = [
    path('', views.index),
    path('contacts', views.contacts),
    path('about', views.about),
    path('news', views.news),
]

urlpatterns = [
    #re_path(r'^index/user/<Login>/<int:Password>', views.user, name='user'),
    path('index/', include (main_page_patterns)),
    path('tables/', include (table_patterns)), 
    re_path(r'^error', views.error, name= 'error'),
    path('login/', views.login),
    path("set", views.set),
    path("get", views.get),
    path('admin/', admin.site.urls),
]
