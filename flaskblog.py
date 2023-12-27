from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '2f814d445f3cdb48676288249364de65e4ca91784e1d58de669efcae8ca84390'

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

if __name__== '__main__' :
    app.run(debug=True)

# Chehcking