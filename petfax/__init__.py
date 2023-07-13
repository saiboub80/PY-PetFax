from flask import Flask

#Factory

def create_app():
    app= Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, PetFax!'
    
    #register pet Blueprint
    
    from . import pet
    app.register_blueprint(pet.bp)

    #return app
    
    return app