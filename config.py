import os

class Config:
    """Base configuration settings."""
    # Flask's 'run' command will automatically load variables from .env
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-hard-to-guess-string'
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')