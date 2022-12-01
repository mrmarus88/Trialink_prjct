#downloaded pack's
import pyodbc as pyo
import mysql.connector
import pandas as pd

#import csv template
main_table = pd.read_csv('D:\\python\\UpdateDB\\new_csv_1.csv',sep='\t',encoding='cp1251')
terminals = pd.DataFrame(main_table)

#Connect with Mysql DB "Trialink"
connect = mysql.connector.connect(user = 'marus',
                                password = 'Banderlog_1',
                                host = 'localhost',
                                database = 'trialink',
                                port = '3306')
cursor = connect.cursor()

insert_stmt = (
    "INSERT INTO terminals (Database_name, Model, Vendor, Model_original, Format, OS, Display, Mobile, LTE_Mode, Radio, WiFi, SIM, GEO, Li_ion, Protect, Mass, Equipment, Description, Remarks)"
    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
)

for row in terminals.itertuples():
            Data = [
                row.Database_name,
                row.Model,
                row.Vendor,
                row.Model_original,
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
            ]
            cursor.execute(insert_stmt,Data)                
   
#Check Dublicates and Delete it
cursor.execute('''
        DELETE
	        terminals
        FROM  
	        terminals
        LEFT OUTER JOIN 
	        (SELECT MIN(id) AS id, DataBase_name FROM terminals GROUP BY DataBase_name) AS tmp
        ON 
	        terminals.id = tmp.id 
        WHERE
	        tmp.id IS NULL
        '''
)

connect.commit() #Close session
connect.close() #close the connection
