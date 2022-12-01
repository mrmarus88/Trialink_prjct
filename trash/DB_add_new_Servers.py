#downloaded pack's
import pyodbc as pyo
import pandas as pd

#import csv template
Servers = pd.read_csv('D:\\Ronet\\UpdateDB\\Servers.csv',sep='\t',encoding='cp1251')
df3 = pd.DataFrame(Servers)

#Connect with SQL DB "Trialink"
connect = pyo.connect('Driver={SQL Server};'
                      'Server=YUMARUS;'
                      'Database=Trialink;'
                      'Trusted_Connection=yes;')
cursor = connect.cursor()

#Fill the table from CSV DataFrame's
for row in df3.itertuples():
    cursor.execute('''
                INSERT INTO Servers (
                DataBase_name,
                Model, 
                Users,
                Design,
                Description,
                Remarks)
                VALUES (?,?,?,?,?)
                ''',
                row.Database_name,
                row.Model,
                row.Users,
                row.Design,
                row.Description,
                row.Remarks               
                )
    
#Check Dublicates and Delete it
cursor.execute('''
        DELETE
	        Servers         
        FROM  
	        Servers
        LEFT OUTER JOIN 
	        (SELECT MIN(id) AS id, DataBase_name FROM Servers GROUP BY DataBase_name) AS tmp
        ON 
	        Servers.id = tmp.id 
        WHERE
	        tmp.id IS NULL
        '''
)

connect.commit() #Close session
