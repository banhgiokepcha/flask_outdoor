from flask import Blueprint, redirect, url_for, render_template
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates'
)


@main_blueprint.route('/')
def index(): 
    return render_template('home.html')

@main_blueprint.route('/login_with_google')
def login_with_google():
    return redirect(url_for('google.login'))


@main_blueprint.route('/welcome')
#@login_required
def welcome():
    return render_template('welcome.html')

