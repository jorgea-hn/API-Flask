from app import create_app
from config import config

enviroment = config['development']
app = create_app()

if __name__ == '__main__':
    app.run()