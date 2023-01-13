from openpyxl import Workbook
import pandas as pd 
import numpy as np
import pretty_html_table
import math


def disc():
    #import xlsx template
    export_values = pd.DataFrame(pd.read_csv('Trialink\\dicriptions.xlsx',sep='\t',encoding='cp1251')).fillna(0)
