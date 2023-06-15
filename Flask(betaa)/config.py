import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object): 
   GOOGLE_MAPS_KEY = 'AIzaSyCJqpC7oo-YYJJ1pRVZJgf84qExlHZCWSc'
   GOOGLE_CLIENT_ID = "352381798381-tnhkl6dmhonckkijldkklucce9d22uik.apps.googleusercontent.com"
   GOOGLE_CLIENT_SECRET = "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"
   SERVER_NAME = '127.0.0.1:5000'
   APPLICATION_ROOT = '/'
   PREFERRED_URL_SCHEME = 'http'
   
class ProdConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'webappmap.db')


class DevConfig(Config):
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'webappmap.db')
    



