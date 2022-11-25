#downloaded pack's
import pyodbc as pyo
import pandas as pd

#import csv template
main_table = pd.read_csv('D:\\Ronet\\UpdateDB\\MAIN.csv',sep='\t',encoding='cp1251')
df = pd.DataFrame(main_table)

#Connect with Mysql DB "Trialink"
connect = pyo.connect('Driver={SQL Server};'
                      'Server=YUMARUS;'
                      'Database=Trialink;'
                      'Trusted_Connection=yes;')
cursor = connect.cursor()

#Fill the table from CSV DataFrame's
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO Main_Table (
                BTS,
                Terminals, 
                Servers,
                Services,
                Others,
                Remarks)
                VALUES (?,?,?,?,?,?)
                ''',
                row.BTS,
                row.Terminals,
                row.Servers,
                row.Services,
                row.Others,
                row.Remarks,
                )
    
#Check Dublicates and Delete it
cursor.execute('''
        DELETE
	        main_table
        FROM  
	        main_table
        LEFT OUTER JOIN 
	        (SELECT MIN(id) AS id, BTS FROM main_table GROUP BY BTS) AS tmp
        ON 
	        main_table.id = tmp.id 
        WHERE
	        tmp.id IS NULL
        '''
)

connect.commit() #Close session
