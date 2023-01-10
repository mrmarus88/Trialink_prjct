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
import datetime
import csv
import pandas as pd
import template as tmp


def news(request):
    return render(request,"news.html")

def index(request):
    return render(request,"index.html")
 
def about(request):
    return render(request,"about.html")
 
def contacts(request):
    return render(request,"contacts.html")

def terminals(request):
    context= {'date': date,
              }
    return render(request,"terminals.html",context)

def bts(request):
    context= {'date': date,
              }
    return render(request,"bts.html",context)

def servers(request):
    context= {'date': date,
              }
    return render(request,"servers.html",context)

def services(request):
    context= {'date': date,
              }
    return render(request,"services.html",context)

@xframe_options_exempt
def test(request):
    context= {'date': date,
              }
    return render(request,"tables/test_table.html",context)

def test1(request):
    return render(request, "tables/test_table_1.html")

def test2(request):
    context= {'date': date,
              }
    return render(request, "tables/test_table_2.html",context)
    
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

date = {'date': ""}

@xframe_options_exempt
def update(request):
    global date
    if request.method == "GET":
        # functionality 1
        rd.sql_request()
        date = datetime.datetime.today().strftime("%d/%m/%Y  %H.%M.%S") # format  2022-04-05  00.18.00
        context= {'date': date,
              }
    elif request.method == "POST":
        # functionality 2 
        rd.sql_request()
        date = datetime.datetime.today().strftime("%d/%m/%Y  %H.%M.%S") # format  2022-04-05  00.18.00
        context= {'date': date,
              }
    return render(request,"main_tables.html",context)


def main_tables(request):
    context= {'date': date,
              }
    return render(request,"main_tables.html",context)


expt = {
        'packet': "",
        'subscribers': "",
        'server_poc': "",
        'enodeb_all': "",
        'non_telrad_enodeb': "",
        'add_42U': "",
        'add_7ubox': "",
        'Router': "",
        'add_SGW': "",
        'add_RGW': "",
        'add_sfp': "",
        'add_l2': "",
        'bts': "",
        'bts_d': "",
        'terminals': "",
        'terminals_type': ""
        }

def calculate(request):
      
    submitbutton= request.POST.get("submit")
    
    packet=''
    subscribers=''
    server_poc=''
    enodeb_all=''
    non_telrad_enodeb=''
    add_42U=''
    add_7ubox=''
    Router=''
    add_SGW=''
    add_RGW=''
    eSFP_10G=''
    L2_service=''
    bts=''
    bts_type=''
    terminals=''
    terminals_type=''
    
       
    form= InputForm(request.POST or None)
    if form.is_valid():
        # process the data in form.cleaned_data as required
        packet = form.cleaned_data.get("packet")
        subscribers = form.cleaned_data.get("subscribers")
        server_poc = form.cleaned_data.get("server_poc")
        enodeb_all = form.cleaned_data.get("enodeb_all")
        non_telrad_enodeb = form.cleaned_data.get("non_telrad_enodeb")
        add_42U = form.cleaned_data.get("add_42U")
        add_7ubox = form.cleaned_data.get("add_7ubox")
        Router = form.cleaned_data.get("Router")
        add_SGW = form.cleaned_data.get("add_SGW")
        add_RGW = form.cleaned_data.get("add_RGW")
        eSFP_10G = form.cleaned_data.get("eSFP_10G")
        L2_service = form.cleaned_data.get("L2_service")
        bts = form.cleaned_data.get("bts")
        bts_type = form.cleaned_data.get("bts_type")
        terminals = form.cleaned_data.get("terminals")
        terminals_type = form.cleaned_data.get("terminals_type")
    
    
    context= {'form': form,
              'packet': packet,
              'subscribers': subscribers,
              'server_poc': server_poc,
              'submitbutton': submitbutton,
              'enodeb_all': enodeb_all,
              'non_telrad_enodeb': non_telrad_enodeb,
              'add_42U': add_42U,
              'add_7ubox': add_7ubox,
              'Router': Router,
              'add_SGW': add_SGW,
              'add_RGW': add_RGW,
              'eSFP_10G': eSFP_10G,
              'L2_service': L2_service,
              'bts': bts,
              'bts_type': bts_type,
              'terminals': terminals,
              'terminals_type': terminals_type,
              }
    
    myData = [{"Position":"packet","Values" : packet},
          {"Position":"subscribers", "Values" : subscribers},
          {"Position":"server", "Values" : server_poc},
          {"Position":"enodeb_all", "Values" : enodeb_all},
          {"Position":"non_telrad_enodeb", "Values" : non_telrad_enodeb},
          {"Position":"add_42U", "Values" : add_42U},
          {"Position":"add_7ubox", "Values" : add_7ubox},
          {"Position":"Router", "Values" : Router},
          {"Position":"add_SGW", "Values" : add_SGW},
          {"Position":"add_RGW", "Values" : add_RGW},
          {"Position":"eSFP_10G", "Values" : eSFP_10G},
          {"Position":"L2_service", "Values" : L2_service},
          {"Position":"bts", "Values" : bts},
          {"Position":"bts_type", "Values" : bts_type},
          {"Position":"terminals", "Values" : terminals},
          {"Position":"terminals_type", "Values" : terminals_type}]


    with open('D:\python\Trialink\Trialink_prjct\Trialink\\test_export.csv', 'w') as csvfile:
        fieldnames = ['Position', 'Values']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerows(myData)
        
    return render(request, 'cs.html', context)


def show_result(request):
    submitbutton= request.POST.get("submit")
    if request.method == "GET":
        # functionality 1
        tmp.calc()
        return render(request,"show_result.html")
    elif request.method == "POST":
        # functionality 2
        tmp.calc()
        return render(request,"show_result.html")


def export_KP(request):
    submitbutton = request.POST.get("export")
    if request.method == "GET":
        # functionality 1
        tmp.calc()
        return render(request,"show_result.html")

    
    

