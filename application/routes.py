# import render_template function from the flask module
from flask import render_template
# import the app object from the ./application/__init__.py
from application import app
# define routes for / & /home, this function will be called when these are accessed

blogData = [
    {  
        "name": {"first":"Wasim", "last":"Danyal"},
        "title":"First Post",
        "content":"My first blog post about Flask"
    },
    {   
        "name": {"first":"Wasim", "last":"Danyal"},
        "title":"Second Post",
        "content":"Even more info"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', posts=blogData)

@app.route('/about')
def about():
    return render_template('about.html', title='about')

@app.route('/login')
def login():
    return render_template('login.html', title='login')

@app.route('/register')
def register():
    return render_template('register.html', title='register')
