import mlab
from models.food import *
import pyexcel
from random import *
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

mlab.connect()
# df = pd.read_excel('Crawdata.xlsx', sheet_name='pyexcel_sheet1')
# dish = ['breakfast', 'lunch', 'dinner']
# for i in df.index:
#   choice_dish = choice(dish)
#   food = Food(title=df['title'][i], img=df['img'][i], nguyenlieu=df['nguyenlieu'][i].strip("\n").replace(" ",""), cachlam=df['cachlam'][i], dish=choice_dish)
#   food.save()
# print("Completed")
food = Food("aaa","aaa","aaa","aaa","aaa")
# food.save()
user = User('ahaha','123456')
user['favorite'].append(food)
# user.save()

print("Completed!")