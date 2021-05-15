from flask import Flask, session
from checker import check_logged_in

app = Flask(__name__)

app.secret_key = "NigdyNieZgadniesz"

@app.route('/')
def hello():
    return "Welcome"

@app.route('/login')
def login():
    session['logged_in']=True
    return 'You are logged in'

@app.route('/logout')
def logout():
    session.pop('logged_in')
    return "You have logged off"

@app.route('/status')
def status():
    if('logged_in' in session):
        return "You are currently logged in"
    else:
        return "You are not currently logged in"

@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    session['user'] = user
    return 'User is:' + session['user']

@app.route('/getuser')
def getuser() -> str:
    return "User current is:" + session['user']

@app.route('/page1')
@check_logged_in
def page1():
    return "First page"

if __name__ == '__main__':
    app.run(debug=True)