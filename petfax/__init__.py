from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from petfax.config import Config
from flask_migrate import Migrate 

db = SQLAlchemy()
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)


    db.init_app(app)
    migrate = Migrate(app,db)
            
    from petfax.pets.routes import pet
    from petfax.fact.routes import fact

    app.register_blueprint(pet)
    app.register_blueprint(fact)

    # return the app 
    return app