from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    name = request.form.get("name")
    return render_template("results.html", name=name)
