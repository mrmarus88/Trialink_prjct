import mysql.connector
 
# Connecting from the server
con = mysql.connector.connect(user = 'marus',
                               password = 'Banderlog_1',
                               host = 'localhost',
                               database = 'trialink',
                               port = '3306')
 
# create cursor object
cursor = con.cursor()
  
# assign data query
query1 = """CREATE TABLE test_3 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Quantity INT,
    Description VARCHAR(100)
)
"""

  
# executing cursor
cursor.execute(query1)
cursor.close()
con.commit()
con.close()