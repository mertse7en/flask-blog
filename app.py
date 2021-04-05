from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = '29031089jsf4564dc'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)


    def __repr__(self): # Reprsent class object as a string okeyyy
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id =db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        "author":'Şeyma Özenbaş',
        "title":"Blog Post 1",
        'content': 'emotional-things',
        'date' : '2021-04-02'
    },
    {
        "author":'Mert Seven',
        "title":"Blog Post 2",
        'content': 'sport',
        'date' : '2021-04-02'
    }
]


@app.route("/")
@app.route("/home")
def get_home():
    return render_template("home.html", title='Home')


@app.route("/about")
def get_about():
    return render_template("about.html", title='About')


@app.route("/posts")
def get_posts():
    return render_template("post.html", posts=posts)

@app.route("/subpart")
def get_subpart():
    return render_template("subpart.html", title='Supbart')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'mert@hotmail.com' and form.password.data == 'password':
            flash("Succesfully Logged in !!", "success")
            return redirect(url_for("get_home"))
        else:
            flash("Login unsuccessfull !Your email or password is wrong !", "success")

    return render_template("login.html", title='Login', form=form)

@app.route("/register", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for("get_home"))
    return render_template("register.html", title='Registration', form=form)

if __name__ == '__main__':
    app.run()





