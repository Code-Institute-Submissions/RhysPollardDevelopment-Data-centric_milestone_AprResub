import os
import random
from flask import (
    Flask, flash, render_template, url_for, redirect, request, session)
from flask_wtf import Form
from wtforms import (
    StringField, PasswordField, BooleanField, SelectField, TextAreaField)
from wtforms.fields import html5
from wtforms.validators import (
    InputRequired, Email, Length, EqualTo, AnyOf, URL, Optional)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    LoginManager, UserMixin, login_user, login_required, logout_user, current_user
)
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User:
    def __init__(self, username):
        self.username = username

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def check_password(password_hash, password):
        return check_password_hash(password_hash, password)

    
@login_manager.user_loader
def load_user(username):
    u = mongo.db.Users.find_one({"Name": username})
    if not u:
        return None
    return User(username=u['Name'])


class RegistrationForm(Form):
    username = StringField(
        # Use of render keywords for html data found at
        # https://pythonpedia.com/en/knowledge-base/20440056/custom-attributes-for
        # -flask-wtforms
        "Username", validators=[InputRequired(), Length(max=20, min=4)],
        render_kw={
            'class': 'form-control',
            'aria-describedby': 'usernameLabel',
            'minlength': '4',
            'maxlength': '20',
            'placeholder': 'Enter username'
        })
    password = PasswordField(
        "Password", validators=[InputRequired(), Length(min=10),
        EqualTo('confirm_password', message="Passwords must match")],
        render_kw={
            'class': 'form-control',
            'aria-describedby': 'passwordLabel',
            'minlength': '10',
            'placeholder': 'Password'
        })
    confirm_password = PasswordField("Repeat Password",
        validators=[InputRequired()],
        render_kw={
            'class': 'form-control',
            'aria-describedby': 'confirmLabel',
            'placeholder': 'Confirm Password'
        })
    email = html5.EmailField("Email", validators=[InputRequired(),
        Email(message='This field requires a valid email')],
        render_kw={
            'class': 'form-control',
            'aria-describedby': 'emailLabel',
            'placeholder': 'Email Address'
        })
    agree = BooleanField("I agree to the terms and conditions of this site.",
        validators=[InputRequired()],
        render_kw={'class':'form-check-input'})


class logInForm(Form):
    login_username = StringField(
        "Username", validators=[InputRequired()],
        render_kw={
            'class': 'form-control',
            'aria-describedby': 'loginUsernameLabel',
            'placeholder': 'Enter username',
            'autocomplete': 'off'
        })
    login_password = PasswordField(
        "Password", validators=[InputRequired()],
        render_kw={
            'class': 'form-control',
            'aria-describedby': 'loginPasswordLabel',
            'placeholder': 'Password'
        })


class Walkform(Form):
    title = StringField("Walking Route Title", validators=[InputRequired(),
        Length(min=5, max=40)],
        render_kw={"class": "form-control",
        "placeholder": "Pendennis point walking loop",
        "minlength":"5", "maxlength":"40"})
        
    difficulty = SelectField("Difficulty", validators=[InputRequired()],
        choices=[], render_kw={"class": "form-control"})

    category_name = SelectField("Walk type", validators=[InputRequired()],
        choices=[], render_kw={"class": "form-control"})

    imageUrl = html5.URLField("Image Url/Address", validators=[InputRequired(),
        Length(min=20, max=250), URL()],
        render_kw={"class": "form-control",
        "placeholder": "Please paste a copied web address/url for the walk's main image",
        "minlength": "20", "maxlength": "250",
        # regex simulated at https://www.regextester.com/20
        "pattern" : "^((http[s]?|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?$"})

    description = StringField("Description", validators=[InputRequired(),
        Length(min=20, max=200)],
        render_kw={"class": "form-control",
        "placeholder": "Pendennis point walking loop",
        "minlength": "20", "maxlength": "200"})
        
    time = StringField("Time", validators=[InputRequired(), Length(max=20)],
        render_kw={"class": "form-control",
        "placeholder": "1 hour 30 minutes", "maxlength": "20"})
        
    startpoint = StringField("Start Point", validators=[InputRequired(),
        Length(min=5, max=40)],
        render_kw={"class": "form-control",
        "placeholder": "Pendennis Carpark",
        "minlength": "5", "maxlength": "40"})
        
    distance = StringField("Distance", validators=[InputRequired(), Length(max=10)],
        render_kw={"class": "form-control",
        "placeholder": "3.5 miles",
        "maxlength": "10"})
        
    dogs_allowed = BooleanField("Dog Friendly",
        render_kw={'class': 'custom-control-input'})
        
    free_parking = BooleanField("Free Parking",
        render_kw={'class': 'custom-control-input'})
        
    paid_parking = BooleanField("Paid Parking",
        render_kw={'class': 'custom-control-input'})

    directions = TextAreaField("Enter your Directions", validators=[InputRequired(),
        Length(min=100, max=1600)],
        render_kw={"class": "form-control",
        "placeholder": "Please enter your directions here.\rNext instruction on a new line without any spaces.\rAnd so on and so forth.",
        "minlength": "100", "maxlength": "1600", "rows":"10"})


class ContactForm(Form):
    problem = SelectField("Report a Problem", validators=[InputRequired()],
        choices=[("Other")], render_kw={"class": "form-control"})
        
    user_issue = TextAreaField("What issue has occurred:", validators=[InputRequired(),
        Length(min=20, max=500)],
        render_kw={"class": "form-control",
        "placeholder": "Tell us what problem you're having and we will try to fix it or get back to you.",
        "minlength": "20", "maxlength": "500", "rows": "7"})
        

class SearchForm(Form):
    query = html5.SearchField("", render_kw={"class": "form-control",
    "placeholder":"Search", "aria-label":"Search"})

    difficulty = SelectField("Difficulty",
    choices=[("Choose...")], render_kw={"class": "form-control"})

    category_name = SelectField("Walk type", choices=[("Choose...")],
    render_kw={"class": "form-control"})
    
    dogs_allowed = BooleanField("Dog Friendly",
        render_kw={'class': 'custom-control-input'})
        
    free_parking = BooleanField("Free Parking",
        render_kw={'class': 'custom-control-input'})
        
    paid_parking = BooleanField("Paid Parking",
        render_kw={'class': 'custom-control-input'})


@app.route("/")
@app.route("/home")
def home():
    """
    Routes user to the home/index page.
    Loads a list of all routes and randomly selects 3 of them to feature.
    """
    # random choices found at w3schools.com
    # https://www.w3schools.com/python/ref_random_choices.asp
    complete = list(mongo.db.routes.find())
    routes = random.choices(complete, k=3)
    return render_template("index.html", routes=routes)


@app.route("/add_walk", methods={"GET", "POST"})
@login_required
def add_walk():
    """ 
    User form to add data for a new walk to the Mongo Database.
    If method is POST, selects all named inputs on form and retrieves info,
    checkboxes are assigned as booleans rather than "On"/"Off" as unchecked
    returns null and is less useful for other logic.
    """
    addform = Walkform()
    # distinct used to select only the fields wanted from collection.
    # https://docs.mongodb.com/manual/reference/method/db.collection.distinct/
    categories = mongo.db.categories.distinct("category_name")
    addform.category_name.choices = [(category, category) for category in categories]

    difficulties = mongo.db.difficulty.find()
    # # cycles through each entry for challenge field to maintain ordering.
    for d in difficulties:
        addform.difficulty.choices.append(d['challenge'])

    if addform.validate_on_submit():
        dogs_allowed = True if request.form.get("dogs_allowed") else False
        free_parking = True if request.form.get("free_parking") else False
        paid_parking = True if request.form.get("paid_parking") else False
        walk = {
            "category_name" : request.form.get("category_name"),
            "title" : request.form.get("title"),
            "description": request.form.get("description"),
            # Split function references from w3 schools at
            # https://www.w3schools.com/python/ref_string_split.asp
            # Split used instead of splitline to maintain carriage return 
            "directions": request.form.get("directions").split("\n"),
            "imageUrl": request.form.get("imageUrl"),
            "difficulty" : request.form.get("difficulty"),
            "time" : request.form.get("time"),
            "distance" : request.form.get("distance"),
            "startpoint" : request.form.get("startpoint"),
            "dogs_allowed" : dogs_allowed,
            "free_parking" : free_parking,
            "paid_parking": paid_parking,
            "user": current_user.username
            #"user": mongo.db.users.find_one(
            #   {"username": session["user"]})["username"]
        }
        mongo.db.routes.insert_one(walk)
        flash("Walk successfully added!")
        return redirect(url_for("user_profile", username=session["user"]))

    return render_template("addwalk.html", addform=addform)


@app.route("/edit_walk/<route_id>", methods={"GET", "POST"})
@login_required
def edit_walk(route_id):
    """ 
    Reloads the add_walk def and pre-fills information to update database.
    Same logic as add_walk but loads walk data using the Object Id.
    """
    categories = mongo.db.categories.distinct("category_name")
    difficulties = mongo.db.difficulty.find()

    # cycles through each entry for challenge field to maintain ordering.
    walk = mongo.db.routes.find_one({'_id': ObjectId(route_id)})
    editform = Walkform(data=walk)
    editform.directions.data = "".join(walk["directions"])
    for d in difficulties:
        editform.difficulty.choices.append(d['challenge'])

    #editform.difficulty.choices = [(challenge, challenge) for challenge in challenges]
    editform.category_name.choices = [(category, category) for category in categories]
    print(editform.directions.data)
    if editform.validate_on_submit():
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
        flash("Walk edited successfully!")
        return redirect(url_for("user_profile", username=session["user"]))

    return render_template("editwalk.html", walk=walk, editform=editform)


@app.route("/delete_walk/<route_id>")
def delete_walk(route_id):
    """ 
    Removes the data for a walk from database collection.
    """
    mongo.db.routes.remove({'_id': ObjectId(route_id)})
    return redirect(url_for("user_profile", username=session["user"]))


@app.route("/show_route/<route_id>")
def show_walk(route_id):
    """
    Selects data for indiviual walk using ObjectId and loads to a template.
    """
    walk = mongo.db.routes.find_one({'_id':ObjectId(route_id)})
    return render_template("walkpage.html", walk=walk)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Loads contact us page with FAQs and form.
    Has a collection which holds frequently asked questions and pre-loaded
    problems to report using form.
    """
    contactform = ContactForm()
    faqs = list(mongo.db.FAQs.find())
    for faq in faqs:
        for f in faq:
            if f == 'report_problem':
                contactform.problem.choices.append(faq[f])

    if contactform.validate_on_submit():
        flash("Your message has been sent, thanks!")
        return redirect(url_for("contact", faqs=faqs, contactform=contactform))
        
    return render_template("contactus.html", faqs=faqs, contactform=contactform)
 

@app.route("/register", methods={"GET", "POST"})
def register():
    """
    Route to registration form if not logged in.
    When form posted, if the user already exists in database the user is 
    redirected to the register page and asked to log in instead.
    """    
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    regform = RegistrationForm()
    if regform.validate_on_submit():
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry, that username already exists")
            return redirect(url_for("register", regform=regform))

        # New user is generated if a matching username is not found.
        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower()
        }
        mongo.db.users.insert_one(new_user)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        #return redirect(url_for("user_profile", username=session["user"], regform=regform))
        return redirect(url_for("user_profile", regform=regform))


    return render_template("register.html", regform=regform)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Loads login page, allows user to insert username and password for database
    comparison.
    If a match is found they are directed to userpage, else returned to
    login with an error message.
    """
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    logform = logInForm()
    if logform.validate_on_submit():
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("login_username").lower()})
            
        if existing_user:
            if check_password_hash(existing_user["password"], request.form.get("login_password")):
                user_obj = User(username=existing_user['username'])
                #session["user"] = request.form.get("login_username").lower()
                print(user_obj.username)
                login_user(user_obj)
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('home')
                return redirect(next_page)
                #return redirect(url_for("user_profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password.")
                return redirect(url_for("login", logform=logform))
        else:
            flash("Incorrect Username and/or Password.")
            return redirect(url_for("login", logform=logform))

    return render_template("login.html", logform=logform)


@app.route("/logout")
def logout():
    """    
    Removes user from session cookie to log them out.
    """
    #session.pop("user")
    logout_user()
    return redirect(url_for("login"))


@app.route("/user_profile/<username>")
#@login_required
def user_profile(username):
    """
    Loads user page which holds a list of all walking routes matching username.
    If no user is logged in, redirect to login page so check it first.
    """
    #username = mongo.db.users.find_one(
    #    {"username": session["user"]})["username"]
    routes = list(mongo.db.routes.find())
    return render_template("userprofile.html", routes=routes)
    #return render_template("userprofile.html", routes=routes, username=username)


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
    # Suggestion of adding to dictionary found on stack overflow
    # https://stackoverflow.com/questions/1024847/how-can-i-add-new-keys-to-a-dictionary
    filters = {}
    filterform = SearchForm()

    categories = mongo.db.categories.distinct("category_name")
    difficulties = mongo.db.difficulty.find()
    # cycles through each entry for challenge field to maintain ordering.
    for d in difficulties:
        filterform.difficulty.choices.append(d['challenge'])

    for c in categories:
        filterform.category_name.choices.append(c)
   
    if request.method == "POST":
        query = request.form.get("query")
        dogs_allowed = request.form.get("dogs_allowed") 
        free_parking = request.form.get("free_parking")
        paid_parking = request.form.get("paid_parking")
        difficulty = request.form.get("difficulty")
        category = request.form.get("category_name")
        
        if query != "":
            filters["$text"] = {"$search": query}
            filterform.query.data=query            

        # Checkboxes added this way so will only limit search for checked boxes,
        # won't select for walks with unchecked boxes, only those with checked.
        if dogs_allowed:
            filters["dogs_allowed"] = True
            filterform.dogs_allowed.data = filters["dogs_allowed"]

        if free_parking:
            filters["free_parking"] = True
            filterform.free_parking.data = filters["free_parking"]
        
        if paid_parking:
            filters["paid_parking"] = True
            filterform.paid_parking.data = filters["paid_parking"]
            
        if difficulty != "Choose...":
            filters["difficulty"] = difficulty
            filterform.difficulty.data = filters["difficulty"]

        if category != "Choose...":
            filters["category_name"] = category
            filterform.category_name.data = filters["category_name"]
            
        routes = list(mongo.db.routes.find(filters))
        if routes == []:
            flash("Nothing matched your search, try changing your search word or filter.", 'error')
        return render_template("searchwalks.html", routes=routes, filterform=filterform, filters=filters)

    routes = list(mongo.db.routes.find())
    return render_template("searchwalks.html", routes=routes, filterform=filterform, filters=filters)


if __name__ == "__main__":
    """
    If the domain name matches __main__ then will load environmental vars.
    """
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)