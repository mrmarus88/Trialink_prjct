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

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

table_patterns  = [
    path("servers", views.servers, name= 'servers'),
    path("services", views.services, name= 'services'),
    path("terminals", views.terminals, name= 'terminals'),
    path("bts", views.bts, name= 'bts'),
    path("test", views.test, name= 'test'),
    path('test1',views.test1, name = "test1"),
    path('test2',views.test2, name = "test2"),
    path('terminals1',views.terminals1, name = "terminals1"),
    path('bts1',views.bts1, name = "bts1"),
    path('servers1',views.servers1, name = "servers1"),
    path('services1',views.services1, name = "services1"),
    path('update', views.update, name = "update"),
]

main_page_patterns = [
    path('', views.index, name= 'home'),
    path('index', views.index, name= 'home'),
    path('contacts', views.contacts, name= 'contacts'),
    path('about', views.about, name= 'about'),
    path('news', views.news, name= 'news'),
    path('profile', views.profile, name='profile'),
    path('trialink', views.trialink, name = 'trialink'),
    path('cs', views.calculate, name= 'cs'),
    #path('test_base', views.calculate, name= 'calculate'),
    path('show_result',views.show_result, name= "show_result"),
]

urlpatterns = [
    path('', include (main_page_patterns), name= 'home'),
    path('tables/', include (table_patterns), name= 'table'),
    path('tables', views.main_tables, name= 'table'),  
    re_path(r'^error', views.error, name= 'error'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('register/login',  auth_views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'registration/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('trialink/', views.trialink, name = 'trialink'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include (router.urls)),
    path('api-auth/', include ('rest_framework.urls', namespace='rest_framework')),
    path('show_result/',views.show_result, name= "show_result"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

