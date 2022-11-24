from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
  
def news(request):
    return render(request,"news.html")

def index(request):
    return render(request,"index.html")
 
def about(request):
    return render(request,"about.html")
 
def contacts(request):
    return render(request,"contacts.html")

def main_tables(request):
    return render(request,"main_tables.html")

def terminals(request):
    return render(request,"terminals.html")

def bts(request):
    return render(request,"bts.html")

def servers(request):
    return render(request,"servers.html")

def services(request):
    return render(request,"services.html")

def login(request):
    return render(request, "login.html")

def logout(request):
    return render(request, "logout.html")

def profile(request):
    return render(request, "profile.html")

def register(request):
    return render(request, "register.html")

def error(request):
    return HttpResponse("Error", status=400, reason="Incorrect data")


#def user(request, Login, Password):
#    return HttpResponse(f"<h2>Login: {Login}  Password:{Password}</h2>")

# установка куки
def set(request):
    # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefined")
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    return response
 
# получение куки
def get(request):
    # получаем куки с ключом username
    username = request.COOKIES["username"]
    return HttpResponse(f"Hello {username}")