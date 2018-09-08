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

@app.route("/contribute")
def contribute():
    return render_template("contribute.html")

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

    return render_template("new.html", list_food_breakfast_html = list_food_breakfast,
    list_food_lunch_html= list_food_lunch,
    list_food_dinner_html=list_food_dinner, img_season=season)

@app.route("/profilepage")
def profilepage():
    return render_template("profilepage.html")

@app.route("/login" , methods = [ 'GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST": 
        users = User.objects()
        form = request.form 
        email = form ['Email']
        password = form ['password']
        flag = False
        for user in users:
            if email == user.email and password == user.password: 
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
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST": 
        form = request.form 
        email = form ['Email']
        password = form ['password']
        first_name = form ["Firstname"]
        last_name = form ["Lastname"]
        createUser = User(email=email,password=password,first_name=first_name,last_name=last_name,favorite = [])
        createUser.save()
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/contribute")
def contribute():
    return render_template("contribute.html")
if __name__ == "__main__":
    app.run(debug=True)