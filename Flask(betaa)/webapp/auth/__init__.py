from flask import (redirect, url_for, session, abort, flash)
from flask_login import LoginManager, AnonymousUserMixin, login_fresh, login_user, current_user
from flask_bcrypt import Bcrypt
from .controllers import google_blueprint
import secrets

class WebAnonymous(AnonymousUserMixin):
    def __init__(self):
        self.username='Guest'

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message="Please login to access this page"
login_manager.anonymous_user=WebAnonymous


def create_module(app, **kwargs):
    secret_key = secrets.token_hex(16)
    app.secret_key = secret_key 
    login_manager.init_app(app)
    app.register_blueprint(google_blueprint)
    
    
@login_manager.user_loader
def load_user(userId):
    from .models import User 
    return User.query.get(userId) 





    
    
