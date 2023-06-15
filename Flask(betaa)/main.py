
from webapp import create_app
import os 

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())


if __name__ == '__main__':
    app.config['SECRET_KEY'] = '5ddb077b78606d6faf6dc133dbe48d378d54526f88f688e7'
    app.run()





