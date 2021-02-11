import os
import random
import math
import ast
from forms import (
    RegistrationForm, LogInForm, WalkForm, ContactForm, SearchForm)
from flask import (
    Flask, flash, render_template, url_for, redirect, request, session)
from flask_pymongo import PyMongo
from wtforms.validators import (
    InputRequired, Email, Length, EqualTo, AnyOf, URL, Optional)
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    """
    Routes user to the home/index page.
    Loads a list of all routes and randomly selects 3 of them to feature.
    """
    # Sets html head tag, idea inspired by
    # https://github.com/faithy80/dcd-project/blob/master/run.py
    page_title = "Welcome To Cornwall"

    # random choices found at w3schools.com
    # https://www.w3schools.com/python/ref_random_sample.asp
    complete = list(mongo.db.routes.find())
    routes = random.sample(complete, k=6)
    return render_template(
        "index.html", routes=routes, page_title=page_title)


@app.route("/add_walk", methods={"GET", "POST"})
def add_walk():
    """
    User form to add data for a new walk to the Mongo Database.
    If method is POST, selects all named inputs on form and retrieves info,
    checkboxes are assigned as booleans rather than "On"/"Off" as unchecked
    returns null and is less useful for other logic.
    """

    page_title = "Add A Walk"

    # If session "user" is not there, redirect to register
    if session.get("user") is None:
        return redirect(url_for("login"))

    addForm = WalkForm()

    # distinct used to select only the fields wanted from collection.
    # https://docs.mongodb.com/manual/reference/method/db.collection.distinct/
    categories = mongo.db.categories.distinct("category_name")
    category_choices = [
        (category, category) for category in categories]
    addForm.category_name.choices.extend(category_choices)

    difficulties = mongo.db.difficulty.find()

    difficulty_choices = []
    # # cycles through each entry for challenge field to maintain ordering.
    for d in difficulties:
        difficulty_choices.append((d["challenge"], d["challenge"]))
    addForm.difficulty.choices.extend(difficulty_choices)

    if addForm.validate_on_submit():
        dogs_allowed = True if request.form.get("dogs_allowed") else False

        free_parking = True if request.form.get("free_parking") else False

        paid_parking = True if request.form.get("paid_parking") else False

        walk = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "description": request.form.get("description"),
            # Split function references from w3 schools at
            # https://www.w3schools.com/python/ref_string_split.asp
            # Split used instead of splitline to maintain carriage return
            "directions": request.form.get("directions").split("\n"),
            "imageUrl": request.form.get("imageUrl"),
            "difficulty": request.form.get("difficulty"),
            "time": request.form.get("time"),
            "distance": request.form.get("distance"),
            "startpoint": request.form.get("startpoint"),
            "dogs_allowed": dogs_allowed,
            "free_parking": free_parking,
            "paid_parking": paid_parking,
            "user": mongo.db.users.find_one(
                {"username": session["user"]})["username"]
        }
        mongo.db.routes.insert_one(walk)
        flash("Walk successfully added!")
        return redirect(url_for(
            "user_profile", username=session["user"]))

    return render_template(
        "addwalk.html", addForm=addForm, page_title=page_title)


@app.route("/edit_walk/<route_id>", methods={"GET", "POST"})
def edit_walk(route_id):
    """
    Reloads the add_walk def and pre-fills information to update database.
    Same logic as add_walk but loads walk data using the Object Id.
    """

    page_title = "Change A Walk"

    walk = mongo.db.routes.find_one_or_404({"_id": ObjectId(route_id)})
    editForm = WalkForm(data=walk)

    # If session "user" is not there, redirect to register.
    if session.get("user") is None:
        return redirect(url_for("login"))
    # If user tries to edit a walk which doesn"t belong to them, redirected.
    elif session.get("user") != walk["user"] and session.get("user") != "admin":
        return redirect(url_for("home"))

    categories = mongo.db.categories.distinct("category_name")
    difficulties = mongo.db.difficulty.find()

    # Cycles through each entry for challenge field to maintain ordering.
    # .data as means to update form code/join found at respectively:
    # https://stackoverflow.com/questions/42984453/wtforms-populate-form-with-
    # data-if-data-exists?noredirect=1&lq=1
    # https://www.w3schools.com/python/ref_string_join.asp
    editForm.directions.data = "".join(walk["directions"])

    # distinct used to select only the fields wanted from collection.
    # https://docs.mongodb.com/manual/reference/method/db.collection.distinct/
    categories = mongo.db.categories.distinct("category_name")
    category_choices = [
        (category, category) for category in categories]
    editForm.category_name.choices.extend(category_choices)

    difficulties = mongo.db.difficulty.find()

    difficulty_choices = []
    # cycles through each entry for challenge field to maintain ordering.
    for d in difficulties:
        difficulty_choices.append((d["challenge"], d["challenge"]))
    editForm.difficulty.choices.extend(difficulty_choices)

    # Only call this if form is submitted and flaskforms validates.
    if editForm.validate_on_submit():

        dogs_allowed = True if request.form.get("dogs_allowed") else False

        free_parking = True if request.form.get("free_parking") else False

        paid_parking = True if request.form.get("paid_parking") else False

        updated = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "description": request.form.get("description"),
            # Splitlines function references from w3 schools at
            # https://www.w3schools.com/python/ref_string_split.asp
            "directions": request.form.get("directions").split("\n"),
            "imageUrl": request.form.get("imageUrl"),
            "difficulty": request.form.get("difficulty"),
            "time": request.form.get("time"),
            "distance": request.form.get("distance"),
            "startpoint": request.form.get("startpoint"),
            "dogs_allowed": dogs_allowed,
            "free_parking": free_parking,
            "paid_parking": paid_parking,
            "user": mongo.db.users.find_one(
                {"username": walk["user"]})["username"]
        }

        mongo.db.routes.update({"_id": ObjectId(route_id)}, updated)
        flash("Walk edited successfully!")
        return redirect(url_for(
            "user_profile", username=walk["user"]))

    return render_template(
        "editwalk.html", walk=walk, editForm=editForm, page_title=page_title)


@app.route("/delete_walk/<route_id>")
def delete_walk(route_id):
    """
    Removes the data for a walk from database collection.
    """
    walk = mongo.db.routes.find_one_or_404({"_id": ObjectId(route_id)})
    mongo.db.routes.remove({"_id": ObjectId(route_id)})
    return redirect(url_for(
        "user_profile", username=walk["user"]))


@app.route("/show_route/<route_id>")
def show_walk(route_id):
    """
    Selects data for indiviual walk using ObjectId and loads to a template.
    Restricts user favouriting their own walk.
    """

    walk = mongo.db.routes.find_one_or_404({"_id": ObjectId(route_id)})

    page_title = walk["title"]

    if session.get("user") is not None:
        user = mongo.db.users.find_one(
            {"username": session["user"]})

        # Checks each id in favourite field array and checks if
        # matches route_id
        favourited = False
        for favourite in user["favourites"]:
            if favourite == route_id:
                favourited = True

        return render_template(
            "walkpage.html", walk=walk, user=user,
            favourited=favourited, page_title=page_title)
    else:
        return render_template(
            "walkpage.html", user=False,
            favourited=False, walk=walk, page_title=page_title)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Loads contact us page with FAQs and form.
    Has a collection which holds frequently asked questions and pre-loaded
    problems to report using form.
    """

    page_title = "How To Contact Us/ FAQs"

    contactForm = ContactForm()
    choices=[]
    faqs = list(mongo.db.FAQs.find())
    for faq in faqs:
        for f in faq:
            if f == "report_problem":
                choices.append((faq[f], faq[f]))
    contactForm.problem.choices.extend(choices)
    
    if contactForm.validate_on_submit():
        message = {
            "Issue": request.form.get("problem"),
            "Message": request.form.get("user_issue")
        }
        mongo.db.messages.insert_one(message)
        flash("Your message has been sent, thanks!")
        return redirect(url_for(
            "contact", faqs=faqs, contactForm=contactForm,
            page_title=page_title))

    return render_template(
        "contactus.html", faqs=faqs, contactForm=contactForm,
        page_title=page_title)


@app.route("/register", methods={"GET", "POST"})
def register():
    """
    Route to registration form if not logged in.
    When form posted, if the user already exists in database the user is
    redirected to the register page and asked to log in instead.
    """

    page_title = "Register Today"

    # If session cookie field "user" exists, then redirects to other page
    if session.get("user") is not None:
        return redirect(url_for("home"))
    regForm = RegistrationForm()
    if regForm.validate_on_submit():
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry, that username already exists")
            return redirect(url_for("register", regForm=regForm))

        # New user is generated if a matching username is not found.
        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower(),
            "favourites": []
        }
        mongo.db.users.insert_one(new_user)

        # put the new user into "session" cookie
        session["user"] = request.form.get("username").lower()
        return redirect(
            url_for(
                "home", username=session["user"], regForm=regForm))

    return render_template(
        "register.html", regForm=regForm, page_title=page_title)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Loads login page, allows user to insert username and password for database
    comparison.
    If a match is found they are directed to userpage, else returned to
    login with an error message.
    """

    page_title = "Login"

    # Code suggestion for identifying cookies found at stack overflow
    # https://stackoverflow.com/questions/28925602/how-can-i-detect-whether
    # -a-variable-exists-in-flask-session/39204060
    if session.get("user") is not None:
        return redirect(url_for("home"))

    logForm = LogInForm()

    if logForm.validate_on_submit():
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("login_username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"],
                    request.form.get("login_password")):
                session["user"] = request.form.get("login_username").lower()
                return redirect(
                    url_for("user_profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password.")
                return redirect(url_for("login", logForm=logForm))
        else:
            flash("Incorrect Username and/or Password.")
            return redirect(url_for("login", logForm=logForm))

    return render_template(
        "login.html", logForm=logForm, page_title=page_title)


@app.route("/logout")
def logout():
    """
    Removes user from session cookie to log them out.
    """
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/user_profile/<username>")
def user_profile(username):
    """
    Loads user page which holds a list of all walking routes matching username.
    If no user is logged in, redirect to login page so check it first.
    """
    page_text = username + "'s Page"
    page_title = page_text.capitalize()

    does_exist = mongo.db.users.find_one_or_404({"username": username})

    if session.get("user") is None:
        flash("Must be logged in to see other`s userpages.", "error")
        return redirect(url_for("register"))

    routes = list(mongo.db.routes.find({"user": username}))

    # Finds the details of the user document for the page owner.
    # Then checks each option in their favourite field and adds the route
    # to a list of routes which can be loaded.
    fav_ids = mongo.db.users.find_one({"username": username})

    favourites = list()
    if fav_ids["favourites"]:
        for f in fav_ids["favourites"]:
            walk = mongo.db.routes.find_one({"_id": ObjectId(f)})
            favourites.append(walk)

    return render_template(
        "userprofile.html", username=username, routes=routes,
        favourites=favourites, page_title=page_title)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Loads search page and a list of all possible walks with other data values.
    Filters is a list which will add database search categories depending on
    which form inputs have been selected. This was done so that an empty query
    string would not return an error.
    Necessary to load prior to is method== POST so empty list can be passed to
    page loading without any search criteria.
    """

    page_title = "Discover Somewhere New"

    page_size = 18

    # https://stackoverflow.com/questions/12455484/
    # checking-for-the-existence-of-a-key-in-request-args-in-flask
    # checks if page_num was in request arguments and updates current page.
    if "page_num" in request.args:
        current_page = int(request.args["page_num"])
    else:
        current_page = 1

    # Suggestion of adding to dictionary found on stack overflow
    # https://stackoverflow.com/questions/1024847/how-can-i-add-new-keys-to-a-dictionary
    filters = {}

    filterForm = SearchForm()

    categories = mongo.db.categories.distinct("category_name")

    difficulties = mongo.db.difficulty.find()

    post = False
    get = False

    # cycles through each entry for challenge field to maintain ordering.
    for d in difficulties:
        filterForm.difficulty.choices.append(d["challenge"])

    for c in categories:
        filterForm.category_name.choices.append(c)

    if request.method == "POST":
        # Post true adds id to results section HTML, this allows javascript
        # to scroll to the div.
        post = True

        query = request.form.get("query")

        dogs_allowed = request.form.get("dogs_allowed")

        free_parking = request.form.get("free_parking")

        paid_parking = request.form.get("paid_parking")

        difficulty = request.form.get("difficulty")

        category = request.form.get("category_name")

        if query != "":
            filters["$text"] = {"$search": query}
            filterForm.query.data = query

        # Checkboxes added this way so will only search for checked boxes,
        # won't select for walks with unchecked boxes, only those with checked.
        if dogs_allowed:
            filters["dogs_allowed"] = True
            filterForm.dogs_allowed.data = filters["dogs_allowed"]

        if free_parking:
            filters["free_parking"] = True
            filterForm.free_parking.data = filters["free_parking"]

        if paid_parking:
            filters["paid_parking"] = True
            filterForm.paid_parking.data = filters["paid_parking"]

        if difficulty != "Choose...":
            filters["difficulty"] = difficulty
            filterForm.difficulty.data = filters["difficulty"]

        if category != "Choose...":
            filters["category_name"] = category
            filterForm.category_name.data = filters["category_name"]

        routes = list(mongo.db.routes.find(filters))
        if routes == []:
            error = (
                "Nothing matched your search,"
                " try changing your search word or filter.")
            flash(
                error,
                "error")

        # Calculates max pages and then selects walks on current page number.
        walks = len(routes)

        max_pages = math.ceil(walks/page_size)

        # skip() and limit() found
        # https://www.codementor.io/@arpitbhayani/
        # fast-and-efficient-pagination-in-mongodb-9095flbqr
        routes = list(
            mongo.db.routes.find(
                filters).sort("title").skip((current_page - 1) * page_size).limit(page_size))

        prev_page = url_for(
            "search", filters=filters,
            page_num=current_page - 1) if current_page > 1 else None
        next_page = url_for(
            "search", filters=filters,
            page_num=current_page + 1) if current_page < max_pages else None

        return render_template(
            "searchwalks.html",
            routes=routes,
            filterForm=filterForm,
            filters=filters,
            post=post,
            page_title=page_title,
            current_page=current_page,
            max_pages=max_pages,
            prev_page=prev_page,
            next_page=next_page)

    # Checks for mention of filters in request.args when changing page, else
    # the POST condition will not be met and results will not be filtered on
    # page change.
    if "filters" in request.args:

        # uses t0_dict() to change arguments from MultiDict to string.
        # https://stackoverflow.com/questions/19680103/
        # flask-convert-request-args-to-dict
        args = request.args.to_dict()

        # converts string to dictionary which is required type.
        # https://stackoverflow.com/questions/988228/
        # convert-a-string-representation-of-a-dictionary-to-a-dictionary
        if args["filters"]:
            filters = ast.literal_eval(args["filters"])

        # Added so page scrolls to results on each new page.
        get = True

        # Checks all keys found in filters and if one matches updates HTML data
        # with the submitted information.
        if "difficulty" in filters.keys():
            filterForm.difficulty.data = filters["difficulty"]
        if "dogs_allowed" in filters.keys():
            filterForm.dogs_allowed.data = filters["dogs_allowed"]
        if "free_parking" in filters.keys():
            filterForm.free_parking.data = filters["free_parking"]
        if "paid_parking" in filters.keys():
            filterForm.paid_parking.data = filters["paid_parking"]
        if "category_name" in filters.keys():
            filterForm.category_name.data = filters["category_name"]
        if "$text" in filters.keys():
            filterForm.query.data = filters["$text"]["$search"]

        routes = list(mongo.db.routes.find(filters).sort("title"))
        if routes == []:
            error = (
                "Nothing matched your search,"
                " try changing your search word or filter.")
            flash(
                error,
                "error")

        walks = len(routes)
        # Calculates max pages and then selects walks on current page number.
        max_pages = math.ceil(walks/page_size)

        routes = list(
            mongo.db.routes.find(filters).sort("title").skip((
                current_page - 1) * page_size).limit(page_size))

        prev_page = url_for(
            "search", filters=filters,
            page_num=current_page - 1) if current_page > 1 else None
        next_page = url_for(
            "search", filters=filters,
            page_num=current_page + 1) if current_page < max_pages else None

        return render_template(
            "searchwalks.html",
            routes=routes,
            filterForm=filterForm,
            filters=filters,
            get=get,
            page_title=page_title,
            current_page=current_page,
            max_pages=max_pages,
            prev_page=prev_page,
            next_page=next_page)
    else:
        walks = len(list(mongo.db.routes.find()))

        max_pages = math.ceil(walks/page_size)

        routes = list(
            mongo.db.routes.find().sort("title").skip((
                current_page - 1) * page_size).limit(page_size))

        prev_page = url_for(
            "search", filters=filters,
            page_num=current_page-1) if current_page > 1 else None
        next_page = url_for(
            "search", filters=filters,
            page_num=current_page + 1) if current_page < max_pages else None

        return render_template(
            "searchwalks.html",
            routes=routes,
            filterForm=filterForm,
            page_title=page_title,
            current_page=current_page,
            max_pages=max_pages,
            prev_page=prev_page,
            next_page=next_page)


@app.route("/toggle_favourite", methods=["POST"])
def toggle_favourite():
    """
    Collects walk id number and checkbox boolean value and either adds walk to
    a favourites array or removes it from the array if checkbox is unchecked.
    """
    # How to access data from ajax found at:
    # https://stackoverflow.com/questions/37631388/
    # how-to-get-data-in-flask-from-ajax-post
    check_box = request.form["checkbox"]

    output = request.form["id"]
    # pushes walk id to user favourite array if check_box is true,
    # removes if false.
    if check_box == "true":
        mongo.db.users.update_one(
            {"username": session["user"]},
            {"$push": {"favourites": output}}
        )
        return "Added"
    else:
        mongo.db.users.update_one(
            {"username": session["user"]},
            {"$pull": {"favourites": output}}
        )
        return "Removed"

    return "Favs"


@app.route("/terms_of_service")
def terms_of_service():
    page_title = "Terms and Conditions"
    return render_template("termsofservice.html", page_title=page_title)


@app.route("/privacy_policy")
def privacy_policy():
    page_title = "Privacy Policy"
    return render_template("privacypolicy.html", page_title=page_title)


@app.errorhandler(404)
def page_not_found(error):
    page_title = "404 Page not found"
    return render_template("404.html", page_title=page_title), 404


@app.errorhandler(500)
def internal_server_error(error):
    page_title = "500 Unexpected Error"
    return render_template("500.html", page_title=page_title), 500


@app.route("/testing")
def testing():
    return render_template("testing.html")


if __name__ == "__main__":
    """
    If the domain name matches __main__ then will load environmental vars.
    """
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
