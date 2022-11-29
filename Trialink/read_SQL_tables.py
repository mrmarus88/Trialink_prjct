
import mysql.connector
import pandas as pd
import pretty_html_table

# Connecting from the server
con = mysql.connector.connect(user = 'marus',
                                    password = 'Banderlog_1',
                                    host = 'localhost',
                                    database = 'trialink',
                                    port = '3306')
# create cursor object
cursor = con.cursor()
query = "Select * from test;"
result_dataFrame = pd.read_sql(query,con)
con.close() #close the connection

#render dataframe as html
html = pretty_html_table.build_table(result_dataFrame, 'blue_light')

#write html to file 
text_file = open("main/templates/tables_pd/test_table_1.html", "w") 
text_file.write(html) 
text_file.close()
