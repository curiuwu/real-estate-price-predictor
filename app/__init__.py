from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt
from .logging_config import configure_logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    configure_logging(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    return app