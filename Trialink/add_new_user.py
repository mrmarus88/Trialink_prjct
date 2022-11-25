import pyodbc as pyo

a = input(str())
b = input(str())

#Connect with SQL DB "Trialink"
connect = pyo.connect('Driver={SQL Server};'
                      'Server=YUMARUS;'
                      'Database=Trialink;'
                      'Trusted_Connection=yes;'
                      'User=admin;'
                      )
cursor = connect.cursor()

#Create a Login + User name with pass like in input
cursor.execute('''
                CREATE LOGIN '''+ a +'''
                WITH PASSWORD = ' '''+ b +''' ',
                DEFAULT_DATABASE = Trialink;
                CREATE USER '''+ a +''' FOR LOGIN '''+ a +''';
                '''
                )
connect.commit() #Close session

