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
from django.urls import path,re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from main import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

table_patterns  = [
    path("servers", views.servers, name= 'servers'),
    path("services", views.services, name= 'services'),
    path("terminals", views.terminals, name= 'terminals'),
    path("bts", views.bts, name= 'bts'),
    path("test", views.test, name= 'test'),
]

main_page_patterns = [
    path('', views.index, name= 'home'),
    path('index', views.index, name= 'home'),
    path('contacts', views.contacts, name= 'contacts'),
    path('about', views.about, name= 'about'),
    path('news', views.news, name= 'news'),
]

urlpatterns = [
    path('', include (main_page_patterns), name= 'home'),
    path('tables/', include (table_patterns), name= 'table'),
    path('tables', views.main_tables, name= 'table'),  
    re_path(r'^error', views.error, name= 'error'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('register/login',  auth_views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'registration/logout.html'), name='logout'),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('api-auth/', include('rest_framework.urls')),
    #path("set", views.set),
    #path("get", views.get),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

