import mysql.connector
import pandas as pd
import pretty_html_table

def sql_request():
    # Connecting from the server
    con = mysql.connector.connect(user = 'marus',
                                    password = 'Banderlog_1',
                                    host = 'localhost',
                                    database = 'trialink',
                                    port = '3306')
    # create cursor object
    cursor = con.cursor()
    #query = "Select * from test;"
    result_dataFrame_test = pd.read_sql("Select * from test;",con)
    result_dataFrame_terminals = pd.read_sql("Select * from terminals;",con)
    result_dataFrame_bts = pd.read_sql("Select * from bts;",con)
    result_dataFrame_servers = pd.read_sql("Select * from servers;",con)
    result_dataFrame_services = pd.read_sql("Select * from services;",con)

    con.close() #close the connection

    #render dataframe as html
    html_test = pretty_html_table.build_table(result_dataFrame_test,'blue_light'
                                                        , font_size='medium'
                                                        #, font_family='Particular'
                                                        , text_align='left'
                                                        , width='auto'
                                                        , index=False)

    #render terminals to html
    html_terminals = pretty_html_table.build_table(result_dataFrame_terminals,'blue_light'
                                                        , font_size='medium'
                                                        #, font_family='Particular'
                                                        , text_align='left'
                                                        , width='auto'
                                                        , index=False)
    #render bts to html
    html_bts = pretty_html_table.build_table(result_dataFrame_bts,'blue_light'
                                                        , font_size='medium'
                                                        #, font_family='Particular'
                                                        , text_align='left'
                                                        , width='auto'
                                                        , index=False)

    #render servers to html
    html_servers = pretty_html_table.build_table(result_dataFrame_servers,'blue_light'
                                                        , font_size='medium'
                                                        #, font_family='Particular'
                                                        , text_align='left'
                                                        , width='auto'
                                                        , index=False)

    #render services to html
    html_services = pretty_html_table.build_table(result_dataFrame_services,'blue_light'
                                                        , font_size='medium'
                                                        #, font_family='Particular'
                                                        , text_align='left'
                                                        , width='auto'
                                                        , index=False)
                                                    
    #write html to file 
    text_file = open("main/templates/tables/test_table_1.html", "w") 
    text_file.write(html_test)
    text_file = open("main/templates/tables/terminals_table_1.html", "w") 
    text_file.write(html_terminals)
    text_file = open("main/templates/tables/bts_table_1.html", "w") 
    text_file.write(html_bts)
    text_file = open("main/templates/tables/servers_table_1.html", "w") 
    text_file.write(html_servers)
    text_file = open("main/templates/tables/services_table_1.html", "w") 
    text_file.write(html_services)


    text_file.close()

sql_request()
