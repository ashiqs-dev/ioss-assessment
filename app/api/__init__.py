from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(
        __name__,
        template_folder='../templates',  # points to templates
        static_folder='../static'        # points to static
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from app.api.routes import url_shortener_bp
    app.register_blueprint(url_shortener_bp)

    with app.app_context():
        db.create_all()

    return app
