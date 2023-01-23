from openpyxl import Workbook
import pandas as pd 
import numpy as np
import template as tmp


def disc():
    
    #Make table Total + Main and format:
    
    
    writer = pd.ExcelWriter('media/results.xlsx')   # create excel writer object
    KP_calc_final.to_excel(writer)                  # write dataframe to excel 
    writer.save()                                   # save the excel 