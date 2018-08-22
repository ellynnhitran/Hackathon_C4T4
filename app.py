from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pagecon")
def pagecon():
    return render_template("pagecon.html")

@app.route("/test")
def test():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)