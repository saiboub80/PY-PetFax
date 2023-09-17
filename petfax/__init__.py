from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from petfax.config import Config
from flask_migrate import Migrate




db = SQLAlchemy()
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from petfax import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
    with app.app_context():
        db.create_all()
            
    from petfax.pets.routes import pet
    from petfax.fact.routes import fact

    app.register_blueprint(pet)
    app.register_blueprint(fact)


    return app