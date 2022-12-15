from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import UserUpdateForm, ProfileUpdateForm
from django.views.decorators.clickjacking import xframe_options_exempt
from django.shortcuts import get_object_or_404
import read_SQL_tables as rd



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

@xframe_options_exempt
def test(request):
    return render(request,"tables/test_table.html")

def test1(request):
    return render(request, "tables/test_table_1.html")

def test2(request):
    return render(request, "tables/test_table_2.html")
    
def terminals1(request):
    return render(request,"tables/terminals_table_1.html")

def bts1(request):
    return render(request,"tables/bts_table_1.html")

def servers1(request):
    return render(request,"tables/servers_table_1.html")

def services1(request):
    return render(request,"tables/services_table_1.html")

def error(request):
    return HttpResponse("Error", status=400, reason="Incorrect data")

def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = UserRegisterForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'registration/profile.html', context)

def trialink(request):
    return redirect("https://trialink.ru/")

@xframe_options_exempt
def update(request):
    if request.method == "GET":
        # functionality 1
        print("1")
        rd.sql_request()
    elif request.method == "POST":
        # functionality 2 
        rd.sql_request()
    return render(request,"main_tables.html")
    