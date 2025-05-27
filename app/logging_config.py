import logging
from logging.handlers import RotatingFileHandler

def configure_logging(app):
    log_level = getattr(logging, app.config["LOG_LEVEL"], logging.INFO)
    handler = RotatingFileHandler(app.config["LOG_FILE"], maxBytes=1000000, backupCount=3)
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
    handler.setFormatter(formatter)
    app.logger.setLevel(log_level)
    app.logger.addHandler(handler)
    app.logger.info("Логирование настроено.")