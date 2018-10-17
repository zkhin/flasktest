from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '8cf9a25bc556a1c8c74a651ececca5c5'

posts = [
    {
        'author': 'Zayar Khin',
        'title': 'Blog Post1',
        'content': 'First post content',
        'date_posted': 'Nov 6, 2018'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post2',
        'content': 'Second post content',
        'date_posted': 'Nov 6, 2018'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
