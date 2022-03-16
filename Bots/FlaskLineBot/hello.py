from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Welcome to SIRLA, {}!</h1>'.format(name)
