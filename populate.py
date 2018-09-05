import mlab
from models.food import *
import pyexcel
from random import *
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

mlab.connect()
df = pd.read_excel('Crawdata.xlsx', sheet_name='pyexcel_sheet1')
dish = ['breakfast', 'lunch', 'dinner']
season = ['winter', 'spring' ,'summer','autumn']
for i in df.index:
  choice_dish = choice(dish)
  choice_season = choice(season)
  food = Food(title=df['title'][i], img=df['img'][i], nguyenlieu=df['nguyenlieu'][i].strip("\n").replace(" ",""), cachlam=df['cachlam'][i], dish=choice_dish, season=choice_season)
  food.save()

print("Completed!")