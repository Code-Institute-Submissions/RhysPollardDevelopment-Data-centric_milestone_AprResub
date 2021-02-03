import re
from flask_wtf import Form
from wtforms import (
    StringField, PasswordField, BooleanField, SelectField, TextAreaField)
from wtforms.fields import html5
from wtforms.validators import (
    InputRequired, Email, Length, EqualTo, AnyOf, URL, Optional)


class RegistrationForm(Form):
    username = StringField(
        # Use of render keywords for html data found at
        # https://pythonpedia.com/en/knowledge-base/20440056/custom-attributes-for
        # -flask-wtforms
        "Username", validators=[InputRequired(), Length(max=20, min=4)],
        render_kw={
            "class": "form-control",
            "aria-describedby": "usernameLabel",
            "minlength": "4",
            "maxlength": "20",
            "placeholder": "Enter username"
        })
    password = PasswordField(
        "Password",
        validators=[
                    InputRequired(),
                    Length(min=10),
                    EqualTo(
                            "confirm_password",
                            message="Passwords must match")],
        render_kw={
                   "class": "form-control",
                   "aria-describedby": "passwordLabel",
                   "minlength": "10",
                   "placeholder": "Password"
        })
    confirm_password = PasswordField(
        "Repeat Password",
        validators=[InputRequired()],
        render_kw={
            "class": "form-control",
            "aria-describedby": "confirmLabel",
            "placeholder": "Confirm Password"
        })
    email = html5.EmailField(
        "Email",
        validators=[
            InputRequired(),
            Email(
                message="This field requires a valid email")],
        render_kw={
            "class": "form-control",
            "aria-describedby": "emailLabel",
            "placeholder": "Email Address"
        })
    agree = BooleanField(
        "I agree to the terms and conditions of this site.",
        validators=[InputRequired()],
        render_kw={"class": "form-check-input"})


class LogInForm(Form):
    login_username = StringField(
        "Username", validators=[InputRequired()],
        render_kw={
            "class": "form-control",
            "aria-describedby": "loginUsernameLabel",
            "placeholder": "Enter username",
            "autocomplete": "off"
        })
    login_password = PasswordField(
        "Password", validators=[InputRequired()],
        render_kw={
            "class": "form-control",
            "aria-describedby": "loginPasswordLabel",
            "placeholder": "Password"
        })


class WalkForm(Form):
    title = StringField(
        "Walking Route Title",
        validators=[
            InputRequired(),
            Length(min=5, max=40)],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter your route title here",
            "minlength": "5", "maxlength": "40"})

    difficulty = SelectField(
        "Difficulty",
        validators=[
            InputRequired()],
        choices=[],
        render_kw={"class": "form-control"})

    category_name = SelectField(
        "Walk type",
        validators=[InputRequired()],
        choices=[],
        render_kw={"class": "form-control"})

    imageUrl = html5.URLField(
        "Image Url/Address",
        validators=[
            InputRequired(),
            Length(min=20, max=250),
            URL()],
        render_kw={
            "class": "form-control",
            "placeholder": ("Please paste a copied web address"
                            "/url for the walk's main image"),
            "minlength": "20", "maxlength": "250",
            # regex simulated at https://www.regextester.com/20
            "pattern": ("^((http[s]?|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)"
                        "([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?$")})

    description = StringField(
        "Description",
        validators=[
            InputRequired(),
            Length(min=20, max=200)],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter a brief description of the walk and area",
            "minlength": "20",
            "maxlength": "200"})

    time = StringField(
        "Time",
        validators=[
            InputRequired(),
            Length(max=20)],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter time estimate",
            "maxlength": "20"})

    startpoint = StringField(
        "Start Point",
        validators=[
            InputRequired(),
            Length(min=5, max=40)],
        render_kw={
            "class": "form-control",
            "placeholder": "Starting landmark or address",
            "minlength": "5",
            "maxlength": "40"})

    distance = StringField(
        "Distance",
        validators=[
            InputRequired(),
            Length(max=10)],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter miles or kilometres",
            "maxlength": "10"})

    dogs_allowed = BooleanField(
        "Dog Friendly",
        render_kw={"class": "custom-control-input"})

    free_parking = BooleanField(
        "Free Parking",
        render_kw={"class": "custom-control-input"})

    paid_parking = BooleanField(
        "Paid Parking",
        render_kw={"class": "custom-control-input"})

    directions = TextAreaField(
        "Enter your Directions",
        validators=[
            InputRequired(),
            Length(min=100, max=1600)],
        render_kw={
            "class": "form-control",
            "placeholder": ("Please enter your directions here.\r"
                            "Next instruction on a new line without"
                            " any spaces.\rAnd so on and so forth."),
            "minlength": "100",
            "maxlength": "1600",
            "rows": "10"})


class ContactForm(Form):
    problem = SelectField(
        "Report a Problem",
        validators=[InputRequired()],
        choices=[("Other")],
        render_kw={"class": "form-control"})

    user_issue = TextAreaField(
        "What issue has occurred:",
        validators=[
            InputRequired(),
            Length(min=20, max=500)],
        render_kw={
            "class": "form-control",
            "placeholder": ("Tell us what problem you're having and "
                            "we will try to fix it or get back to you."),
            "minlength": "20",
            "maxlength": "500",
            "rows": "7"})


class SearchForm(Form):
    query = html5.SearchField(
        "",
        render_kw={
            "class": "form-contol",
            "placeholder": "Search by location or keyword",
            "aria-label": "Search"})

    difficulty = SelectField(
        "Difficulty",
        choices=[("Choose...")],
        render_kw={"class": "form-control"})

    category_name = SelectField(
        "Walk type",
        choices=[("Choose...")],
        render_kw={"class": "form-control"})

    dogs_allowed = BooleanField(
        "Dog Friendly",
        render_kw={"class": "custom-control-input"})

    free_parking = BooleanField(
        "Free Parking",
        render_kw={"class": "custom-control-input"})

    paid_parking = BooleanField(
        "Paid Parking",
        render_kw={"class": "custom-control-input"})
