#downloaded pack's
import pyodbc as pyo
import pandas as pd

#import csv template
Terminals = pd.read_csv('D:\\Ronet\\UpdateDB\\Terminals.csv',sep='\t',encoding='cp1251')
df4 = pd.DataFrame(Terminals)

#Connect with SQL DB "Trialink"
connect = pyo.connect('Driver={SQL Server};'
                      'Server=YUMARUS;'
                      'Database=Trialink;'
                      'Trusted_Connection=yes;')
cursor = connect.cursor()

#Fill the table from CSV DataFrame's
for row in df4.itertuples():
    cursor.execute('''
                INSERT INTO Terminals (
                Database_name,
                Model,
                Format,
                OS,
                Display,
                Mobile,
                LTE_Mode,
                Radio,
                WiFi,
                SIM,
                GEO,
                Li_ion,
                Protect,
                Mass,
                Equipment,
                Description,
                Remarks)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''',
                row.Database_name,
                row.Model,
                row.Format,
                row.OS,
                row.Display,
                row.Mobile,
                row.LTE_Mode,
                row.Radio,
                row.WiFi,
                row.SIM,
                row.GEO,
                row.Li_ion,
                row.Protect,
                row.Mass,
                row.Equipment,
                row.Description,
                row.Remarks               
                )
    
#Check Dublicates and Delete it
cursor.execute('''
        DELETE
	        Terminals
        FROM  
	        Terminals
        LEFT OUTER JOIN 
	        (SELECT MIN(id) AS id, DataBase_name FROM Terminals GROUP BY DataBase_name) AS tmp
        ON 
	        Terminals.id = tmp.id 
        WHERE
	        tmp.id IS NULL
        '''
)

connect.commit() #Close session
