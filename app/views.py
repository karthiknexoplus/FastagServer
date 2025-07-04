from flask import Blueprint, render_template, redirect, url_for, flash, request, session, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from datetime import datetime
from .forms import LoginForm, SignupForm

main = Blueprint('main', __name__)

def get_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return 'Good Morning'
    elif 12 <= hour < 18:
        return 'Good Afternoon'
    elif 18 <= hour < 22:
        return 'Good Evening'
    else:
        return 'Welcome'

@main.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('main.dashboard'))
    return redirect(url_for('main.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    greeting = get_greeting()
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            current_app.logger.info(f"User {username} logged in.")
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid username or password', 'danger')
            current_app.logger.warning(f"Failed login attempt for username: {username}")
    return render_template('login.html', greeting=greeting, form=form)

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    greeting = get_greeting()
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        if User.query.filter((User.username==username)|(User.email==email)).first():
            flash('Username or email already exists', 'danger')
            current_app.logger.warning(f"Signup attempt with existing username/email: {username}/{email}")
        else:
            user = User(username=username, email=email, password_hash=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            current_app.logger.info(f"New user registered: {username}")
            flash('Account created! Please log in.', 'success')
            return redirect(url_for('main.login'))
    return render_template('signup.html', greeting=greeting, form=form)

@main.route('/logout')
def logout():
    user_id = session.pop('user_id', None)
    current_app.logger.info(f"User {user_id} logged out.")
    greeting = get_greeting()
    flash('You have been logged out.', 'info')
    return render_template('logout.html', greeting=greeting)

@main.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('dashboard.html', user=user)
    return redirect(url_for('main.login')) 