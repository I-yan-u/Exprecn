#/usr/bin/python3
"""
Web app with flask
"""
from flask import Flask, render_template, url_for, redirect, request, session
from models import store
from models.user import User
from models.history import UserHistory
from hashlib import md5


app = Flask(__name__)
app.secret_key = 'AUGGACUAG'

loggedin_menu = ['About', 'History', 'Profile', 'Log Out']
loggedout_menu = ['Log In', 'Sign Up', 'About']


@app.teardown_appcontext
def close(error):
    """ shuts down DB"""
    return store.close()

@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home():
    """ Landing page"""
    if 'user' not in session:
        return render_template('home.html', menu=loggedout_menu)
    if 'user' in session:
        return render_template('home.html', menu=loggedin_menu, id=session['user']['id'], name=session['user']['first_name'])

@app.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def login():
    """ Login page"""
    if request.method == 'POST':
        email = request.form['email']
        psswd = request.form['password']
        psswd = md5(psswd.encode()).hexdigest()
        user_by_mail = store.get_user_email(email)
        if user_by_mail != None and user_by_mail.password == psswd:
            session['user'] = user_by_mail.to_dict()
            return redirect(url_for('home', logged=True))
        else:
            return redirect(url_for('login', logged=False))
    else:
        if 'user' in session:
            return redirect(url_for('home', logged=True))
        return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'], strict_slashes=False)
def signup():
    """ Signup page"""
    if request.method == 'POST':
        new_user_data = request.form
        new_user = User(**new_user_data)
        store.new(new_user)
        store.save()
        session['user'] = new_user.to_dict()
        return redirect(url_for('home', logged=True))
    return render_template('signup.html')

@app.route('/about', methods=['GET'], strict_slashes=False)
def about():
    """ About page"""
    if 'user' in session:
        return render_template('about.html', menu=loggedin_menu)
    else:
        return render_template('about.html', menu=loggedout_menu)

@app.route('/profile', methods=['GET', 'POST'], strict_slashes=False)
def profile():
    """ Profile page"""
    user_profile = session.get('user', None)
    id = user_profile.get('id', None)
    user_hist = store.get_hist_user(id)

    if user_profile:
        return render_template('profile.html', menu=loggedin_menu,
                               user=user_profile)
    else:
        return redirect(url_for('login'))

@app.route('/history', methods=['GET', 'POST'], strict_slashes=False)
def history():
    """ User History page"""
    user_profile = session.get('user', None)
    id = user_profile.get('id', None)
    user_hist = store.get_hist_user(id)

    if user_profile:
        return render_template('history.html', menu=loggedin_menu,
                               history=user_hist,
                               id=session['user']['id'])
    else:
        return redirect(url_for('login'))

@app.route('/logout', methods=['GET'], strict_slashes=False)
def logout():
    """ Logout page"""
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)