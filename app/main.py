from flask import Flask
from app.api.routes import url_shortener_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(url_shortener_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
