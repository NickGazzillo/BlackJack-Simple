# imports
import random as r
import pandas as pd
import numpy as np
from openpyxl import load_workbook
random = r.randint(1, 3)
#files 
if random == 1:
    file = pd.DataFrame({
        'Col 1':[1],
        'Col 2':[0],
        'Col 3':[0]
    })
if random == 2:
    file = pd.DataFrame({
        'Col 1':[0],
        'Col 2':[1],
        'Col 3':[0]
    })
if random == 3:
    file = pd.DataFrame({
        'Col 1':[0],
        'Col 2':[0],
        'Col 3':[1]
    })
print(random)
filePath = 'BlackJack.xlsx'
ExcelWorkbook = load_workbook(filePath)
writer = pd.ExcelWriter(filePath, engine = 'openpyxl')
file.to_excel(writer, sheet_name='dataPage')
writer.save()
writer.close()