from flask import Flask
from config import Config

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register the main blueprint
    from .main.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # --- UNCOMMENT THE THREE LINES BELOW ---
    from .api.routes import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app