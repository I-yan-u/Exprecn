#/usr/bin/python3
"""
Web app with flask
"""
from flask import Flask, render_template, url_for, redirect, request, session
from models import store

app = Flask(__name__)
app.secret_key = 'AUGGACUAG'

loggedin_menu = ['About', 'History', 'Profile', 'Log Out']
loggedout_menu = ['Log In', 'Sign Up', 'About']

@app.teardown_appcontext
def close(error):
    """ shuts down DB"""
    return store.close()

@app.route('/', strict_slashes=False)
def home():
    """ Landing page"""
    if 'user' not in session:
        menu = ['Log In', 'Sign Up']
        return render_template('home.html', menu=loggedout_menu)
    if 'user' in session:
        return render_template('home.html', menu=loggedin_menu)

@app.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def login():
    """ Login page"""
    if request.method == 'POST':
        user = request.form['email']
        session['user'] = user
        return redirect(url_for('home', logged=True))
    else:
        if 'user' in session:
            return redirect(url_for('home', logged=True))
        return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'], strict_slashes=False)
def signup():
    """ Signup page"""
    return render_template('signup.html')

@app.route('/about', methods=['GET'], strict_slashes=False)
def about():
    """ About page"""
    return render_template('about.html', menu=loggedin_menu)

@app.route('/profile', methods=['GET', 'POST'], strict_slashes=False)
def profile():
    """ Profile page"""
    return render_template('profile.html', menu=loggedin_menu)

@app.route('/history', methods=['GET', 'POST'], strict_slashes=False)
def history():
    """ User History page"""
    return render_template('history.html', menu=loggedin_menu)

@app.route('/logout', methods=['GET'], strict_slashes=False)
def logout():
    """ Logout page"""
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)