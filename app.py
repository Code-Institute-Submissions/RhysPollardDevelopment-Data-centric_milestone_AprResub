import os
import random
from flask import (
    Flask, flash, render_template, url_for, redirect, request, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Index/landing page
# Loads 3 walks for viewer as todays pic at random.
@app.route("/")
@app.route("/home")
def home():
    # random choices found at w3schools.com
    # https://www.w3schools.com/python/ref_random_choices.asp
    complete = list(mongo.db.routes.find())
    routes = random.choices(complete, k=3)
    return render_template("index.html", routes=routes)


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
            # https://www.w3schools.com/python/ref_string_split.asp
            "directions": request.form.get("directions").split("\n"),
            "imageUrl": request.form.get("imageUrl"),
            "difficulty" : request.form.get("difficulty"),
            "time" : request.form.get("time"),
            "distance" : request.form.get("distance"),
            "startpoint" : request.form.get("startpoint"),
            "dogs_allowed" : dogs_allowed,
            "free_parking" : free_parking,
            "paid_parking": paid_parking,
            "user": mongo.db.users.find_one(
                {"username": session["user"]})["username"]
        }
        mongo.db.routes.insert_one(walk)
        return redirect(url_for("home"))

    categories = mongo.db.categories.find()
    difficulties = mongo.db.difficulty.find()
    return render_template("addwalk.html", categories=categories, difficulties=difficulties)


@app.route("/edit_walk/<route_id>", methods={"GET","POST"})
def edit_walk(route_id):
    if request.method == "POST":
        dogs_allowed = True if request.form.get("dogs_allowed") else False
        free_parking = True if request.form.get("free_parking") else False
        paid_parking = True if request.form.get("paid_parking") else False
        updated = {
            "category_name" : request.form.get("category_name"),
            "title" : request.form.get("title"),
            "description": request.form.get("description"),
            # Splitlines function references from w3 schools at
            # https://www.w3schools.com/python/ref_string_split.asp
            "directions": request.form.get("directions").split("\n"),
            "imageUrl": request.form.get("imageUrl"),
            "difficulty" : request.form.get("difficulty"),
            "time" : request.form.get("time"),
            "distance" : request.form.get("distance"),
            "startpoint" : request.form.get("startpoint"),
            "dogs_allowed" : dogs_allowed,
            "free_parking" : free_parking,
            "paid_parking": paid_parking,
            "user": mongo.db.users.find_one(
                {"username": session["user"]})["username"]
        }
        mongo.db.routes.update({'_id': ObjectId(route_id)}, updated)
        return redirect(url_for("home"))

    walk = mongo.db.routes.find_one({'_id': ObjectId(route_id)})
    categories = mongo.db.categories.find()
    difficulties = mongo.db.difficulty.find()
    return render_template("editwalk.html", walk=walk, categories=categories, difficulties=difficulties)


@app.route("/delete_walk/<route_id>")
def delete_walk(route_id):
    mongo.db.routes.remove({'_id': ObjectId(route_id)})
    return redirect(url_for("home"))


@app.route("/show_route/<route_id>")
def show_walk(route_id):
    walk = mongo.db.routes.find_one({'_id':ObjectId(route_id)})
    return render_template("walkpage.html", walk=walk)


@app.route("/contact")
def contact():
    faqs = list(mongo.db.FAQs.find())
    return render_template("contactus.html", faqs=faqs)


@app.route("/register", methods={"GET", "POST"})
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            return redirect(url_for("register"))

        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(new_user)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        return redirect(url_for("user_profile", username=session["user"]))

    return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = request.form
        existing_user = mongo.db.users.find_one(
            {"username": form.get("username").lower()})
        
        if existing_user:
            if check_password_hash(existing_user["password"], form.get("password")):
                session["user"] = form.get("username").lower()
                return redirect(url_for("user_profile", username=session["user"]))
            else:
                return redirect(url_for("login"))
        else:
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    #removes user from session cookie.
    session.pop("user")
    return redirect(url_for("login"))



@app.route("/user_profile/<username>")
def user_profile(username):
    # If no user is logged in, redirect to login page so check it first.
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    routes = list(mongo.db.routes.find())
    return render_template("userprofile.html", username=username, routes=routes)


@app.route("/search_page")
def search_page():
    routes = list(mongo.db.routes.find())
    categories = mongo.db.categories.find()
    difficulties = mongo.db.difficulty.find()
    return render_template("searchwalks.html", routes=routes, categories=categories, difficulties=difficulties)


@app.route("/search", methods=["GET", "POST"])
def search():
# Suggestion of adding to dictionary found on stack overflow
# https://stackoverflow.com/questions/1024847/how-can-i-add-new-keys-to-a-dictionary
    filters = {}
    if request.method == "POST":
        query = request.form.get("query")
        dogs_allowed = request.form.get("dogs_allowed") 
        free_parking = request.form.get("free_parking")
        paid_parking = request.form.get("paid_parking")
        difficulty = request.form.get("difficulty")
        category = request.form.get("category_name")
        

        if query != "":
            filters["$text"] = {"$search": query}

        if dogs_allowed:
            filters["dogs_allowed"] = True
            
        if free_parking:
            filters["free_parking"] = True
        
        if paid_parking:
            filters["paid_parking"] = True
            
        if difficulty != "Choose...":
            filters["difficulty"] = difficulty

        if category != "Choose...":
            filters["category_name"] = category

        print(filters)
        
        routes = list(mongo.db.routes.find(filters))
        categories = mongo.db.categories.find()
        difficulties = mongo.db.difficulty.find()
        return render_template("searchwalks.html", routes=routes, categories=categories, difficulties=difficulties, filters=filters)

    routes = list(mongo.db.routes.find())
    categories = mongo.db.categories.find()
    difficulties = mongo.db.difficulty.find()
    return render_template("searchwalks.html", routes=routes, categories=categories, difficulties=difficulties, filters=filters)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)