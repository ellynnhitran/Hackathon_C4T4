import mlab
from models.food import Food
import pyexcel
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

mlab.connect()
df = pd.read_excel('Crawdata.xlsx', sheet_name='pyexcel_sheet1')

for i in df.index:
  food = Food(title=df['title'][i], img=df['img'][i], nguyenlieu=df['nguyenlieu'][i].strip("\n").replace(" ",""), cachlam=df['cachlam'][i])
  # food.save()
print("Completed")