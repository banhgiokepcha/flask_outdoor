import secrets

def create_module(app, **kwargs):
    secret_key = secrets.token_hex(16)
    app.secret_key = secret_key 
    from .controllers import app_blueprint

    app.register_blueprint(app_blueprint)
