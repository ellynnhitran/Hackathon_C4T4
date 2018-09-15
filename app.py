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

_flag = False
user_current = {}
page_current = None
# ADMIN START
@app.route("/admin")
def admin():
    if 'admin' in session:
        return render_template("admin.html")
    else:
        return redirect(url_for('login'))

@app.route("/admin/<int:choose>", methods=['POST','GET'])
def admin_choose(choose):
    if request.method == 'GET':
        if 'admin' not in session:
            return redirect(url_for('login'))
        else:
            if choose == 1:
                user = Users.objects()
                return render_template("admin/admin_user.html", users =user)
            elif choose == 2:
                food = Food.objects()
                return render_template("admin/admin_food.html", food = food)

@app.route("/admin/2/queue", methods=['POST','GET'])
def admin_queue():
    if request.method == 'GET':
        if 'admin' not in session:
            return redirect(url_for('login'))
        else:
            food = Food.objects(checked=False)
            return render_template("admin/admin_food_queue.html", food = food)

@app.route('/admin/<int:choose>/delete/<id>', methods = ['GET', 'POST'])
def admin_delete(choose,id):
    if choose == 1:
        user_delete = Users.objects(id = id)
        user_delete.delete()
        return redirect(url_for('admin_choose', choose = 1))
    if choose == 2:
        food_delete = Food.objects(id = id)
        food_delete.delete()
        return redirect(url_for('admin_choose', choose = 2))

@app.route('/admin/<int:choose>/edit/<id>', methods = ['GET', 'POST'])
def admin_edit(choose,id):
    if request.method == 'GET':
        if choose == 1:     
            user = Users.objects(id = id)
            return render_template('admin/admin_edit/edit_user.html', user = user)
        elif choose == 2:
            food = Food.objects(id = id)
            Season = ['spring','autumn','summer','winter']
            Dish = ['breakfast', 'lunch', 'dinner']
            Select_Season = food[0].season
            Season.remove(food[0].season)

            Dish_Select = food[0].dish
            Dish.remove(food[0].dish)
            return render_template('admin/admin_edit/edit_food.html', food = food, select_season = Select_Season,
            season=Season, dish_select = Dish_Select, dish = Dish)
    elif request.method == 'POST':
        form = request.form
        if form['choose'] == '1':
            user = Users.objects(id = id)
            last_name = form['lastname']
            first_name = form['firstname']
            password = form['password']
            user.update(set__last_name = last_name)
            user.update(set__first_name = first_name)
            user.update(set__password = password)
            return redirect(url_for('admin_choose', choose = form['choose']))
        elif form['choose'] == '2':
            food = Food.objects(id = id)
            title = form['title']
            img = form['img']
            nguyenlieu = form['nguyenlieu']
            cachlam = form['cachlam']
            bua = form['bua']
            mua = form['mua']
            food.update(set__title = title)
            food.update(set__img = img)
            food.update(set__nguyenlieu = nguyenlieu)
            food.update(set__cachlam = cachlam)
            food.update(set__dish = bua)
            food.update(set__season = mua)
            return redirect(url_for('admin_choose', choose = form['choose']))

@app.route('/admin/checking/<id>')
def checking(id):
    food = Food.objects(id = id)
    if food[0]['checked'] == True:
        food.update(set__checked = False)
    else:
        food.update(set__checked = True)
    return redirect(url_for('admin_choose', choose = 2))

# ADMIN_END
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contribute")
def contribute():
    return render_template("contribute.html")

@app.route("/pagecon2/<string:getID>", methods = ["POST", "GET"])
def pagecon2(getID):
    global _flag, user_current, page_current
    page_current = request.url
    if request.method == "GET":
        query_food_with_id = Food.objects().with_id(getID)
        saved = False
        if (user_current != {}):
            for food_in_user in user_current.favorite:
                if query_food_with_id.id == food_in_user.id:
                    saved = True
        if (query_food_with_id.author is not None):
            author_with_id = Users.objects().with_id(query_food_with_id.author)
        else:
            author_with_id = {
                'email': 'anonymous@gmail.com',
                'first_name': 'Anonymous',
                'last_name': '',  
            }
        #Random Recommend
        food_random = Food.objects(dish = query_food_with_id.dish, season = query_food_with_id.season, checked=True)
        all_data = list((food_random))
        shuffle(all_data)
        save_food = all_data[:5]
        return render_template("pagecon2.html", food = query_food_with_id, user_current = user_current,  _flag = _flag, saved=saved, author_with_id = author_with_id, recommend = save_food)
    elif request.method == "POST":
        form = request.form
        if form['contribute'] == "3":
            title = form['Title']
            img = form['Image']
            nguyenlieu = form['nguyenlieu']
            cachlam = form['cachlam']
            dish = form['dish']
            season = form['season']
            author = str(user_current.id)
            new_food = Food(title = title, img = img, nguyenlieu = nguyenlieu, cachlam = cachlam, checked = False,dish = dish, season = season, author = author )
            new_food.save()
            user = Users.objects(id = user_current.id)
            user.update(push__posted = new_food)
            user_current.posted = user[0]['posted']
            return redirect(request.url)
        return redirect(request.url)

@app.route("/option/<string:season>", methods = ["POST", "GET"])
def option(season):
    global _flag, user_current, page_current
    page_current = request.path
    if request.method == 'GET':
        list_food_breakfast = Food.objects(dish="breakfast", season = season, checked=True)
        list_food_lunch = Food.objects(dish="lunch",season = season, checked=True)
        list_food_dinner = Food.objects(dish="dinner", season = season, checked=True)

        return render_template("new.html", list_food_breakfast_html = list_food_breakfast,
        list_food_lunch_html= list_food_lunch,
        list_food_dinner_html=list_food_dinner, img_season=season, user_current = user_current, _flag = _flag)
    elif request.method == "POST":
        form = request.form
        if form['contribute'] == "3":
            title = form['Title']
            img = form['Image']
            nguyenlieu = form['nguyenlieu']
            cachlam = form['cachlam']
            dish = form['dish']
            season = form['season']
            author = str(user_current.id)
            new_food = Food(title = title, img = img, nguyenlieu = nguyenlieu, cachlam = cachlam, checked = False,dish = dish, season = season, author = author )
            new_food.save()
            user = Users.objects(id = user_current.id)
            user.update(push__posted = new_food)
            user_current.posted = user[0]['posted']
            return redirect(request.url)
        return redirect(request.url)

@app.route("/profilepage", methods = ["POST", "GET"])
def profilepage():
    global _flag, user_current, page_current
    page_current = request.url
    if 'loggin' not in session:
        return redirect(url_for('login'))
    else:
        if user_current is not None:
            get_user_current = Users.objects().with_id(user_current.id)
            return render_template("profilepage.html", _flag = _flag, user_current=get_user_current)

@app.route("/delete/fav/<id>")
def delete_fav(id):
    food = Food.objects().with_id(id)
    get_user_current = Users.objects(id = user_current.id)
    get_user_current.update(pull__favorite = food)
    return redirect(url_for('profilepage'))


@app.route("/login" , methods = [ 'GET', 'POST'])
def login():
    global _flag, user_current, page_current
    if request.method == "GET":
        if 'loggin' in session:
            return redirect(url_for('home'))
        return render_template("login.html")
    elif request.method == "POST": 
        users = Users.objects()
        form = request.form 
        email = form ['Email']
        password = form ['password']
        flag = False
        flagAdmin = False
        if email == 'admin@gmail.com' and password == 'admindeptrai':
                flagAdmin = True
        for user in users:
            if email == user.email and password == user.password:
                user_current = user
                flag = True
        if (flag):
            session['loggin'] = True
            _flag = True 
            return redirect(page_current)

        elif (flagAdmin):
            session['admin'] = True
            return redirect(url_for('admin'))

        else:
            flash ("Username or Password Wrong!")
            return render_template("login.html")

@app.route("/fav/<id>")
def fav(id):
    global user_current
    if user_current == {}:
        return redirect(url_for('login'))
    if 'loggin' in session:
        user = Users.objects(id = user_current.id)
        food = Food(id = id)
        user.update(push__favorite = food)
        user.update(push__posted = food)
        user_current.favorite = user[0]['favorite']
        user_current.favorite = user[0]['posted']
        return redirect(url_for('pagecon2', getID = id))
    else:
        return redirect(url_for('login'))

@app.route("/logout")
def logout():
    global _flag, user_current, page_current
    page_current = request.url
    if 'loggin' in session:
        _flag = False
        del session['loggin']
        user_current = {}
        return redirect(url_for("home"))
    return redirect(url_for("login"))
 
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        list_users = Users.objects()
        form = request.form 
        email = form ['Email']
        password = form ['password']
        first_name = form ["Firstname"]
        last_name = form ["Lastname"]
        for user in list_users:
            if user.email == email:
                flash ("Your Email had been existed! ")
                return render_template("signup.html")
        createUser = Users(email=email,password=password,first_name=first_name,last_name=last_name,favorite = [])
        createUser.save()
        return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)