from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        # Create tables if they don't exist
        db.create_all()

        # Import routes
        from . import routes

        return app
