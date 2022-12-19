import datetime
from flask import render_template
from flask import Flask


app = Flask(__name__) 

@app.route('/main/templates')
def today():
    date = datetime.datetime.today().strftime("%d/%m/%Y  %H.%M.%S") # format  2022-04-05  00.18.00
    return render_template('base_table.html',date = date)

date2 = datetime.datetime.today().strftime("%d/%m/%Y  %H.%M.%S") # format  2022-04-05  00.18.00
print(date2)