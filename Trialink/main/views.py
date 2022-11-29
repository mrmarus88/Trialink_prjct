from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserForm
from .forms import NewUserForm, UserUpdateForm, ProfileUpdateForm


  
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

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})


def test(request):
    return render(request,"tables/test_table.html")

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
            messages.success(request, f'Profile updated.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'registration/profile.html', context)