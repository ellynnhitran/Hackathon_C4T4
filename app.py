from flask import *
from models.food import *
from random import *
import mlab
import bson
app = Flask(__name__)

mlab.connect()

@app.route("/")
def home():
    list_food_breakfast = Food.objects(dish="breakfast")
    list_food_lunch = Food.objects(dish="lunch")
    list_food_dinner = Food.objects(dish="dinner")
    count = 0
    _5FoodBreakfast = []
    for food in list_food_breakfast:
        if (count < 5):
            _5FoodBreakfast.append(choice(list_food_breakfast))
            count += 1
        else:
            count = 0
            break
    _5FoodLunch = []
    for food in list_food_lunch:
        if (count < 5):
            _5FoodLunch.append(choice(list_food_lunch))
            count += 1
        else:
            count = 0
            break
    _5FoodDinner = []
    for food in list_food_dinner:
        if (count < 5):
            _5FoodDinner.append(choice(list_food_dinner))
            count += 1
        else:
            count = 0
            break
    return render_template("new.html", list_food_breakfast_html = _5FoodBreakfast,
    list_food_lunch_html= _5FoodLunch,
    list_food_dinner_html=_5FoodDinner)

@app.route("/pagecon")
def pagecon():
    return render_template("pagecon.html")
@app.route("/pagecon2/<string:getID>")
def pagecon2(getID):
    query_food_with_id = Food.objects().with_id(getID)
    print(query_food_with_id)

    return render_template("pagecon2.html", food = query_food_with_id)

@app.route("/test")
def test():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)