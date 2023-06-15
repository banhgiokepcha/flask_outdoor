from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text
 

db = SQLAlchemy()
migrate=Migrate()

"""The create_app() function is the application factory, which takes as an argument the name of 
a configuration to use for the application. The configuration settings stored in one of the classes
defined in config.py can be imported directly into the application using the from_object() method
available in Flask’s app.config configuration object. The configuration object is selected
by name from the config dictionary. Once an application is created and configured,
the extensions can be initialized. Calling init_app() on the extensions that were created
earlier completes their initialization."""

def page_not_found(error):
    return render_template('404.html'), 404 

def create_app(object_name):
    """Flask application factory"""
    app = Flask(__name__, static_folder='static')

    app.config.from_object(object_name)
    

    db.init_app(app)
    migrate.init_app(app, db)
    from .auth import create_module as google_create_module
    from .main import create_module as main_create_module
    from .web import create_module as web_create_module
    #from .web import creat
    with app.app_context():
     google_create_module(app)
     main_create_module(app)
     web_create_module(app)
    
    return app
    
   
