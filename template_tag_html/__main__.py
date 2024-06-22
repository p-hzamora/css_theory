from flask import Flask
from app.config import Config


def create_app(config_class=Config):
    from app.components.city import bp as city_bp

    app = Flask(__name__, template_folder="/templates", static_folder="static")
    app.config.from_object(config_class)

    app.register_blueprint(city_bp, url_prefix="/city")

    return app


create_app().run(port=5000)

