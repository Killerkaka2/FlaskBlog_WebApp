from flask import render_template, url_for, flash, redirect
from flask_login import current_user, login_user, logout_user
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User,Post

posts = [
    {
        'author' : "Corey Schafer",
        'title' : "Blog Post 1",
        'content' : "First Blog Post",
        'date_posted':"26 April, 2023"
    },
    {
        'author' : "Pranav",
        'title' : "Blog Post 2",
        'content' : "Second Blog Post",
        'date_posted':"20 April, 2018"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    # Creating object (Instance of the Class)
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)   #Creating a new obj/user(Instance of class User)
        db.session.add(user)
        db.session.commit()
        flash('Your Account has been created! You can now Log In','success')
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    # Creating object (Instance of the Class)
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Failed. Invalid email and Password','danger')
    return render_template("login.html", title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
# Restriction before logging in
def account():
    return render_template('account.html', title='Account')