
from .. import db
from . import AnonymousUserMixin



class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False)
    user_name = db.Column(db.String(255), nullable=False)

    def __init__(self, email="", id="", user_name=""):
        self.email = email
        self.user_name = user_name


    def __repr__(self):
        return '<User {}>'.format(self.user_name)
    
    
    @property
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin ):
            return False
        else:
            return True 
        
    def get_id(self):
        return str(self.id)
    
    def is_active(self):
        # Replace this condition with your own logic to determine if the user is active
        return True