# Russian text in CSV by pandas
# encoding='cp1251' 
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

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


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