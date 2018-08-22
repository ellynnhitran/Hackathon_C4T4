import mlab
from models.food import Food
import pyexcel
a = pyexcel.Sheet()
print(a)
mlab.connect()

food = Food(title="bbbbb", img="iohoih", nguyenlieu="oijpj", cachlam="hihi")

food.save()