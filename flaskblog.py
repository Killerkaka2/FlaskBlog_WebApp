from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author' : "Corey Schafer",
        'title' : "Blog Post 1",
        'Comments' : "First Blog Post",
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
    return render_template("about.html")


if __name__== '__main__' :
    app.run(debug=True)

# Chehcking