import os
from flask import (
    Flask, flash, render_template, url_for, redirect, request, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Index/landing page
@app.route("/")
@app.route("/home")
def home():
    routes = list(mongo.db.routes.find())
    return render_template("base.html", routes=routes)


@app.route("/add_walk",methods={"GET","POST"})
def add_walk():
    if request.method == "POST":
        dogs_allowed = True if request.form.get("dogs_allowed") else False
        free_parking = True if request.form.get("free_parking") else False
        paid_parking = True if request.form.get("paid_parking") else False
        walk = {
            "category_name" : request.form.get("category_name"),
            "title" : request.form.get("title"),
            "description": request.form.get("description"),
            # Splitlines function references from w3 schools at
            # https://www.w3schools.com/python/ref_string_splitlines.asp
            "directions" : request.form.get("directions").splitlines(),
            "difficulty" : request.form.get("difficulty"),
            "time" : request.form.get("time"),
            "distance" : request.form.get("distance"),
            "startpoint" : request.form.get("startpoint"),
            "dogs_allowed" : dogs_allowed,
            "free_parking" : free_parking,
            "paid_parking" : paid_parking
        }
        mongo.db.routes.insert_one(walk)
        return redirect(url_for("home"))

    categories = mongo.db.categories.find()
    return render_template("addwalk.html", categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)


