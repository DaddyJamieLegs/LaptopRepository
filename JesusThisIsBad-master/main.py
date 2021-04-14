from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/home")
def index():
    return render_template('home.html')

@app.route("/about")
def template_test():
    return render_template('about.html')

@app.route("/register")
def template():
    return render_template('register.html')

@app.route("/login")
def template1():
    return render_template('login.html')


app.run()