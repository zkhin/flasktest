from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Zayar Khin',
        'title': 'Blog Post1',
        'content': 'First post content',
        'date_posted': 'Nov 6, 2018'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True)
