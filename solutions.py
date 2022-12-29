Russian text in CSV by pandas
encoding='cp1251' 
import pandas as pd
# example:
data_rus = pd.read_csv(r'D:\\Ronet\\UpdateDB\\test\\normal.csv',sep='\t',encoding='cp1251')
print(data_rus)

# add pic in html
# <img src="{% static "images/back.jpg" %}" alt="winter 2022" >

#start\off venv server
#  python manage.py runserver 
#  deavtivate #server 

#migration
# python manage.py migrate

#create admin-superuser
# python manage.py createsuperuser

#Примечание: если вы забыли пароль суперпользователя, его можно сменить так: 
# python manage.py changepassword <имя пользователя

#Для обновления структуры базы создадим и выполним миграции:
# сначала запустим python manage.py makemigrations, 
# а затем python manage.py migrate.

#Запустим Джанго-команду для создания нового приложения под названием users: 
# python manage.py startapp users


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

try:
    with connect(
        host="localhost",
        user=input("Имя пользователя: "),
        password=getpass("Пароль: "),
        database = "trialink",
        port = '3306',
    ) as connection:
        print(connection)
except Error as e:
    print(e)

test_table_query = """
CREATE TABLE test(
    id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Quantity INT,
    Description VARCHAR(100),
)
"""

with connection.cursor() as cursor:
    cursor.execute(test_table_query)
    connection.commit()
    


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

#Commercial solution - get input from html
def calculate(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':     
        # create a form instance and populate it with data from the request:                   
        form= UserForm(request.POST)
        
        # check it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            packet = form.cleaned_data["packet"]
            subscribers = form.cleaned_data["subscribers"]
            enodeball = form.cleaned_data["enodeball"]
            nontelradenodeb = form.cleaned_data["nontelradenodeb"]
            bts = form.cleaned_data["bts"]
            bts_d = form.cleaned_data["bts_d"]
            terminals = form.cleaned_data["terminals"]
            
        context= {'form': form,
                #'submitbutton': submitbutton,
                'packet': packet,
                'subscribers':subscribers,
                'enodeball':enodeball,
                'nontelradenodeb':nontelradenodeb,
                'bts':bts,
                'bts_d':bts_d,
                'terminals':terminals}
        # redirect to a new URL:   
        return render(request, 'cs.html', context)
            
    
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()
        
    return render(request, 'cs.html', {'form': form})


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
    
    context= {'form': form, 'firstname': firstname,
              'lastname':lastname, 'submitbutton': submitbutton,
              'emailvalue':emailvalue}
    
    return render(request, 'show_result.html', context)


from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table,TableStyle,colors


def export():
    tmp.vers_exp() 


    c_width=[1*inch] # width of the columns 
    t=Table(export_vers,colWidths=c_width,repeatRows=1)
    t.setStyle(TableStyle([('FONTSIZE',(0,0),(-1,-1),12),
                           ('BACKGROUND',(0,0),(-1,0),colors.lightgreen),('VALIGN',(0,0),(-1,0),'TOP')]))
    elements=[]
    elements.append(t)
    export_vers.build(elements)
    print(export_vers)


