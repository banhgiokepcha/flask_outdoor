import os
from webapp import create_app, db, migrate
from webapp.auth.models import User
from webapp.web.models import Markers, Activity, Places

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Markers=Markers, Activity=Activity, Places=Places,migrate=migrate)



 
 