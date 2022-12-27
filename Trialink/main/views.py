from tracemalloc import start
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from requests import request
from .forms import Test2Form, UserRegisterForm, UserUpdateForm, ProfileUpdateForm,InputForm
from django.views.decorators.clickjacking import xframe_options_exempt
from django.shortcuts import get_object_or_404
import read_SQL_tables as rd
import template as tmp


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

def show_result_calc(request):
    return render(request,"show_result_calc.html")

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
        rd.sql_request()
    elif request.method == "POST":
        # functionality 2 
        rd.sql_request()
    return render(request,"main_tables.html")


def calculate(request):
      
    submitbutton= request.POST.get("submit")
    
    packet=''
    subscribers=''
    enodeb_all=''
    non_telrad_enodeb=''
    add_42U=''
    add_7ubox=''
    add_router=''
    add_SGW=''
    add_RGW=''
    add_sfp=''
    add_l2=''
    bts=''
    bts_d=''
    terminals=''
    
    form= InputForm(request.POST or None)
    if form.is_valid():
        # process the data in form.cleaned_data as required
        packet = form.cleaned_data.get("packet")
        subscribers = form.cleaned_data.get("subscribers")
        enodeb_all = form.cleaned_data.get("enodeb_all")
        non_telrad_enodeb = form.cleaned_data.get("non_telrad_enodeb")
        add_42U = form.cleaned_data.get("add_42U")
        add_7ubox = form.cleaned_data.get("add_7ubox")
        add_router = form.cleaned_data.get("add_router")
        add_SGW = form.cleaned_data.get("add_SGW")
        add_RGW = form.cleaned_data.get("add_RGW")
        add_sfp = form.cleaned_data.get("add_sfp")
        add_l2 = form.cleaned_data.get("add_l2")
        bts = form.cleaned_data.get("bts")
        bts_d = form.cleaned_data.get("bts_d")
        terminals = form.cleaned_data.get("terminals")
    
    
    context= {'form': form,
              'packet': packet,
              'subscribers': subscribers,
              'submitbutton': submitbutton,
              'enodeb_all': enodeb_all,
              'non_telrad_enodeb': non_telrad_enodeb,
              'add_42U': add_42U,
              'add_7ubox': add_7ubox,
              'add_router': add_router,
              'add_SGW': add_SGW,
              'add_RGW': add_RGW,
              'add_sfp': add_sfp,
              'add_l2': add_l2,
              'bts': bts,
              'bts_d': bts_d,
              'terminals': terminals,
              }
    
    return render(request, 'cs.html', context)


def show_result(request):
    submitbutton= request.POST.get("submit")
    
    firstname=''
    lastname=''
    emailvalue=''
    
    form= Test2Form(request.POST or None)
    if form.is_valid():
        firstname= form.cleaned_data.get("first_name")
        lastname= form.cleaned_data.get("last_name")
        emailvalue= form.cleaned_data.get("email")
    

    context= {'form': form,
              'firstname': firstname,
              'lastname':lastname,
              'submitbutton': submitbutton,
              'emailvalue':emailvalue}
    
    return render(request, 'show_result.html', context)

def export_KP(request):
    submitbutton = request.POST.get("export")
    if request.method == "GET":
        # functionality 1
        tmp.export()
    elif request.method == "POST":
        # functionality 2 
        tmp.export()
    return HttpResponse