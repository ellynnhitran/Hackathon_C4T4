from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("new.html")

@app.route("/pagecon")
def pagecon():
    return render_template("pagecon.html")
@app.route("/pagecon2")
def pagecon2():
    return render_template("pagecon2.html")

@app.route("/test")
def test():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)