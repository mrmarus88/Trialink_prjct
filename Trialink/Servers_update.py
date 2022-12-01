#downloaded pack's
import pyodbc as pyo
import mysql.connector
import pandas as pd

#import csv template
main_table = pd.read_csv('D:\\python\\UpdateDB\\new_csv_2.csv',sep='\t',encoding='cp1251')
servers = pd.DataFrame(main_table)

#Connect with Mysql DB "Trialink"
connect = mysql.connector.connect(user = 'marus',
                                password = 'Banderlog_1',
                                host = 'localhost',
                                database = 'trialink',
                                port = '3306')
cursor = connect.cursor()


insert_stmt = (
        "INSERT INTO Servers (DataBase_name, Model, Users, Design, Description)"
        "VALUES (%s,%s,%s,%s,%s)")

#Fill the table from CSV DataFrame's
for row in servers.itertuples():
                Data = [row.DataBase_name, row.Model, row.Users, row.Design, row.Description]
                cursor.execute(insert_stmt, Data)
    
#Check Dublicates and Delete it
cursor.execute('''
        DELETE
	        servers         
        FROM  
	        servers
        LEFT OUTER JOIN 
	        (SELECT MIN(id) AS id, DataBase_name FROM servers GROUP BY DataBase_name) AS tmp
        ON 
	        servers.id = tmp.id 
        WHERE
	        tmp.id IS NULL
        '''
)

connect.commit() #Close session
