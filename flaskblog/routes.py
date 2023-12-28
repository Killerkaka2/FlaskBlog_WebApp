from flask import render_template, url_for, flash, redirect
from flaskblog import app
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
    # Creating object (Instance of the Class)
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    # Creating object (Instance of the Class)
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been Logged In!!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Failed. Invalid Username and Password','danger')
    return render_template("login.html", title='Login', form=form)
