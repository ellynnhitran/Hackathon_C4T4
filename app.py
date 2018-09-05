from flask import *
from models.food import *
from random import *
import webbrowser
import os
import mlab
import bson
app = Flask(__name__)
app.config['SECRET_KEY'] = "xp{v~8Zp8jcxj2wd`;5"
mlab.connect()

@app.route("/", methods = ["POST", "GET"])
def home():
    return render_template("index.html")

@app.route("/pagecon")
def pagecon():
    return render_template("pagecon.html")

@app.route("/pagecon2/<string:getID>")
def pagecon2(getID):
    query_food_with_id = Food.objects().with_id(getID)
    print(query_food_with_id)

    return render_template("pagecon2.html", food = query_food_with_id)

@app.route("/option/<string:season>")
def option(season):
    list_food_breakfast = Food.objects(dish="breakfast", season = season)
    list_food_lunch = Food.objects(dish="lunch",season = season)
    list_food_dinner = Food.objects(dish="dinner", season = season)
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
    list_food_dinner_html=_5FoodDinner, img_season=season)

@app.route("/profilepage")
def profilepage():
    return render_template("profilepage.html")

@app.route("/login" , methods = [ 'GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST": 
        users = User.objects()
        print(users)
        form = request.form 
        email = form ['Email']
        password = form ['password']
        flag = False
        for user in users:
            if email == user.username and password == user.password: 
            # valid credential
                flag = True
                
        if (flag):
            session ['Email'] = email
            return redirect('/profilepage')
        else:
            flash ("Username or Password Wrong!")
            return render_template("login.html")

@app.route("/logout")
def logout():
    if session['Email']:
        del session['Email']
    return render_template("login.html")
 
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)