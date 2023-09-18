from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from petfax.config import Config
from flask_migrate import Migrate




db = SQLAlchemy()
def create_app(config_class=Config):
    appliction = Flask(__name__)
    appliction.config.from_object(Config)

    from petfax import models
    models.db.init_app(appliction)
    migrate = Migrate(appliction, models.db)
    with appliction.app_context():
        db.create_all()
            
    from petfax.pets.routes import pet
    from petfax.fact.routes import fact

    appliction.register_blueprint(pet)
    appliction.register_blueprint(fact)


    return appliction