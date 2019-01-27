from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from smartag.config import Config


db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from smartag.main.routes import main
    from smartag.errors.handlers import errors
    from smartag.plants.routes import plants

    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(plants)
    
    return app

