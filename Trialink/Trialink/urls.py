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
from main import views


table_patterns  = [
    path("servers", views.servers),
    path("services", views.services),
    path("terminals", views.terminals),
    path("bts", views.bts),
]

main_page_patterns = [
    path('index', views.index, name= 'home'),
    path('contacts', views.contacts),
    path('about', views.about),
    path('news', views.news),
]

urlpatterns = [
    path('', include (main_page_patterns), name= 'home'),
    path('index/', include (main_page_patterns), name= 'home'),
    path('tables/', include (table_patterns), name= 'table'),
    path('tables', views.main_tables, name= 'table'),  
    re_path(r'^error', views.error, name= 'error'),
    #path("set", views.set),
    #path("get", views.get),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

