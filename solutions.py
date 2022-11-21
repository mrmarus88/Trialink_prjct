# Russian text in CSV by pandas
# encoding='cp1251' 
import pandas as pd
# example:
data_rus = pd.read_csv(r'D:\\Ronet\\UpdateDB\\test\\normal.csv',sep='\t',encoding='cp1251')
print(data_rus)


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