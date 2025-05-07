from flask import Flask
from app.routes.exercise_routes import exercise_routes

def create_app():
    app = Flask(__name__)
    
    # Mendaftarkan blueprint
    app.register_blueprint(exercise_routes)

    return app
